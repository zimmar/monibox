create table cfg_overviewboxes
(
    id        int auto_increment
        primary key,
    name      varchar(35) not null,
    label     varchar(35) not null,
    sortorder tinyint     not null
)
    collate = utf8_unicode_ci;

INSERT INTO tsmmonitor.cfg_overviewboxes (id, name, label, sortorder) VALUES (1, 'healthdata', 'Health Status', 10);
INSERT INTO tsmmonitor.cfg_overviewboxes (id, name, label, sortorder) VALUES (2, 'database', 'TSM Database', 20);
INSERT INTO tsmmonitor.cfg_overviewboxes (id, name, label, sortorder) VALUES (3, 'totaldata', 'Total Data', 30);
INSERT INTO tsmmonitor.cfg_overviewboxes (id, name, label, sortorder) VALUES (4, 'schedules', 'Schedule Status', 40);