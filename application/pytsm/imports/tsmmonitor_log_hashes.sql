create table log_hashes
(
    tablename varchar(255) not null,
    hash      varchar(255) not null,
    constraint tablename
        unique (tablename)
)
    collate = utf8_unicode_ci;

alter table log_hashes
    add primary key (tablename);

