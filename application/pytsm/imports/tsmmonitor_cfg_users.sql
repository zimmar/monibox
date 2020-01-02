create table cfg_users
(
    id         int auto_increment
        primary key,
    username   varchar(35)                       not null,
    password   varchar(32)                       not null,
    stylesheet varchar(35) default 'default.css' not null,
    role       varchar(35)                       not null
)
    collate = utf8_unicode_ci;

INSERT INTO tsmmonitor.cfg_users (id, username, password, stylesheet, role) VALUES (1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'style_silver.css', 'admin');