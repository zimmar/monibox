create table cfg_mainmenu
(
    id        int auto_increment
        primary key,
    name      varchar(35) not null,
    label     varchar(35) not null,
    sortorder smallint    not null
)
    collate = utf8_unicode_ci;

INSERT INTO tsmmonitor.cfg_mainmenu (id, name, label, sortorder) VALUES (1, 'nodes', 'Nodes', 10);
INSERT INTO tsmmonitor.cfg_mainmenu (id, name, label, sortorder) VALUES (2, 'server', 'Server', 20);
INSERT INTO tsmmonitor.cfg_mainmenu (id, name, label, sortorder) VALUES (3, 'backup', 'Backup / Archive', 30);
INSERT INTO tsmmonitor.cfg_mainmenu (id, name, label, sortorder) VALUES (4, 'schedules', 'Schedules', 40);
INSERT INTO tsmmonitor.cfg_mainmenu (id, name, label, sortorder) VALUES (5, 'activity', 'Activity', 50);
INSERT INTO tsmmonitor.cfg_mainmenu (id, name, label, sortorder) VALUES (6, 'serverstorage', 'Server Storage', 60);
INSERT INTO tsmmonitor.cfg_mainmenu (id, name, label, sortorder) VALUES (7, 'offsite', 'Offsite Management', 70);