create table cfg_servers
(
    id            int auto_increment
        primary key,
    servername    varchar(35)      not null,
    description   varchar(35)      not null,
    ip            varchar(15)      not null,
    port          int(5)           not null,
    username      varchar(35)      not null,
    password      varchar(35)      not null,
    libraryclient int(1) default 0 not null,
    `default`     int(1) default 0 not null
)
    collate = utf8_unicode_ci;

