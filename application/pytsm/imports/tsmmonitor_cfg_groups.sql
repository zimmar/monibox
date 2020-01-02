create table cfg_groups
(
    id      int auto_increment
        primary key,
    `group` varchar(35) default 'users' not null
)
    collate = utf8_unicode_ci;

INSERT INTO tsmmonitor.cfg_groups (id, `group`) VALUES (1, 'testgroup');