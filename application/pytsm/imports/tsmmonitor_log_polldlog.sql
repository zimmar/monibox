create table log_polldlog
(
    timestamp              int         not null,
    servername             varchar(30) not null,
    Updated                int         not null,
    `Not Changed`          int         not null,
    `Pollfreq Not Reached` int         not null,
    timeneeded             int         not null
)
    collate = utf8_unicode_ci;

