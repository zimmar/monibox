create table cfg_config
(
    id          int auto_increment
        primary key,
    confkey     varchar(35)  not null,
    confval     varchar(255) not null,
    description varchar(255) not null
)
    collate = utf8_unicode_ci;

INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (1, 'timeout', '200', 'change this value to your desired php timeout');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (2, 'version', 'new_install', 'TSM Monitor version');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (3, 'path_tmlog', '', 'TSM Monitor Logfile Path');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (4, 'path_polldlog', '', 'PollD Logfile Path');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (5, 'loglevel_tm', 'INFO', 'TSM Monitor Log Level');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (6, 'loglevel_polld', 'INFO', 'PollD Log Level');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (7, 'path_dsmadmc', '', 'dsmadmc Binary Path');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (8, 'path_php', '', 'PHP Binary Path');
INSERT INTO tsmmonitor.cfg_config (id, confkey, confval, description) VALUES (9, 'polld_maxproc', '5', 'PollD maximum concurrent processes');