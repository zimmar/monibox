from __future__ import absolute_import
from __future__ import unicode_literals


from pytz import unicode
from six.moves import configparser

import subprocess
import sys
import string
import os
import re
import csv
from django.conf import settings

def _default_message_handler(msg_prefix, msg_number, msg_type, msg_text):
    sys.stderr.write("%s%s%s %s\n" %
                     (msg_prefix, msg_number, msg_type, msg_text))


class Failed(Exception):
    pass

blacklist_msg_numbers = {
    '0944',  # ANR0944E QUERY PROCESS: No active processes found.
    '2034',  # ANR2034E SELECT: No match found using this criteria.
    '8001',  # ANS8001I Return code 11
    '2034',  # dsmadmc runs correctly but result is empty (e.g. processes)
    '1017',  # Systemfehler
    '8023',

}


def _decode_n_char(n, char):
    if char in string.whitespace:
        if char == " " or char == "\n":
            return char
    elif char in string.printable:
        return char
    return "%%%02X" % n


def _decode(line):
    # decode line as utf-8, but if error then strip out all non-ASCII
    # characters
    try:
        return line.decode("utf-8")
    except UnicodeDecodeError:
        return "".join(map(_decode_char, line))


if sys.version_info < (3, 0):
    # Python2: csv module does not support unicode, we must use byte strings.

    def _decode_char(char):
        # char is string
        return _decode_n_char(ord(char), char)

    def _input_csv(csv_data):
        for line in csv_data:
            assert isinstance(line, bytes)
            yield line

    def _output_csv(csv_line):
        for i, column in enumerate(csv_line):
            csv_line[i] = _decode(column)
            assert isinstance(csv_line[i], unicode)

else:
    # Python3: csv module does support unicode, we must use strings everywhere,
    # not byte strings

    def _decode_char(char):
        # char is integer
        return _decode_n_char(char, chr(char))

    def _input_csv(unicode_csv_data):
        for line in unicode_csv_data:
            assert isinstance(line, bytes)
            line = _decode(line)
            assert isinstance(line, str)
            yield line

    def _output_csv(csv_line):
        for column in csv_line:
            assert isinstance(column, str)


class dsmadmc(object):

    def __init__(self):
        self.message_handler = _default_message_handler

    def open(self, server, user, password, logfile):
        self.server = server
        self.user = user
        self.password = password
        self.logfile = logfile
        print("Instanz wwurde geöffnet.")

    def close(self):
        print("Instanz geschlossen.")

    def set_message_handler(self, message_handler):
        self.message_handler = message_handler

    def _message(self, msg_prefix, msg_number, msg_type, msg_text):
        self.message_handler(msg_prefix, msg_number, msg_type, msg_text)

    def auto_open(self, server):
        configfile = os.path.join(os.getenv('HOME'), '.pytsm', 'pytsm.conf')
        logfile = os.path.join(os.getenv('HOME'), '.pytsm', 'dsmerror.log')
        config = configparser.RawConfigParser()
        config.read(configfile)
        if server is None:
            server = config.get("main", 'default_server')
        user = config.get(server, 'user')
        password = config.get(server, 'password')
        self.open(server, user, password, logfile)

    def execute(self, command, args=None):
        server = self.server
        user = self.user
        password = self.password
        logfile = self.logfile

        if args is not None:
            command = command % self.literal(args)

        command = command.replace('NOTEQUAL', '<>')
        command = command.replace('EQUAL', '==')
        command = command.replace('LESS', "<")

        print(command)

        if not settings.BASE_DIR:
            BASE_DIR = "T:/develop/monibox"
        else:
            BASE_DIR = settings.BASE_DIR

        if sys.platform == 'win32':
            cmd = [
                "C:/Program Files/Tivoli/TSM/baclient/dsmadmc",
                "-optfile=%s" % (BASE_DIR + "/optfiles/" + server + ".opt"),
            ]
        else:
            cmd = [
                "/usr/bin/dsmadmc",
            ]

        cmd += [
            "-servername=%s" % server,
            "-id=%s" % user,
            "-password=%s" % password,
            "-ERRORLOGNAME=%s" % logfile,
            "-comma",  "-dataonly=yes", command]


        print(cmd)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        reader = csv.reader(
            _input_csv(process.stdout), delimiter=str(","))

        for row in reader:
            _output_csv(row)
            print(row)
            m = re.match("([A-Z][A-Z][A-Z])(\d\d\d\d)([IESWK]) (.*)$", row[0])
            if m is not None:
                if m.group(2) not in blacklist_msg_numbers:
                    self._message(
                        m.group(1), m.group(2), m.group(3),
                        m.group(4) + ",".join(row[1:]))
            else:
                yield row

        retcode = process.wait()
        if retcode and retcode != 11:
            cmd[3] = "-password=XXXXXXXXXX"  # don't put the password on stderr
            cmd_str = " ".join(cmd)
            raise Failed(
                "Command '%s' returned non-zero exit status %d\n"
                % (cmd_str, retcode))

    def literal(self, o):
        result_array = []
        for v in o:
            v = str(v)
            v = v.replace("'", "\\'")
            result_array.append("'" + v + "'")
        return tuple(result_array)
