create table log_polldstat
(
    id      tinyint(1) default 1 not null,
    enabled int(1)     default 1 not null,
    status  varchar(35)          not null,
    lastrun int                  null,
    nextrun int                  null
)
    collate = utf8_unicode_ci;

INSERT INTO tsmmonitor.log_polldstat (id, enabled, status, lastrun, nextrun) VALUES (1, 0, '', 0, 0);