create table cfg_pytsm_config
(
    cfg_pytsm_config_confkey     varchar(255),
    cfg_pytsm_config_confval     varchar(255),
    cfg_pytsm_config_description varchar(255),
    cfg_pytsm_config_id          integer
);

alter table cfg_pytsm_config
    owner to postgres;

INSERT INTO pytsm.cfg_pytsm_config (cfg_pytsm_config_confkey, cfg_pytsm_config_confval, cfg_pytsm_config_description, cfg_pytsm_config_id) VALUES ('timeout', '200', 'Max Value to run a query', 0);
INSERT INTO pytsm.cfg_pytsm_config (cfg_pytsm_config_confkey, cfg_pytsm_config_confval, cfg_pytsm_config_description, cfg_pytsm_config_id) VALUES ('path_dsmadmc', 'c:/program files/tivoli/tsm/baclient/dsmadmc.exe', 'Tivoli Command line tool', 1);
INSERT INTO pytsm.cfg_pytsm_config (cfg_pytsm_config_confkey, cfg_pytsm_config_confval, cfg_pytsm_config_description, cfg_pytsm_config_id) VALUES ('path_polldlog', 't:/develop/monibox/application/logs/polld.log', 'Debug information', 3);
INSERT INTO pytsm.cfg_pytsm_config (cfg_pytsm_config_confkey, cfg_pytsm_config_confval, cfg_pytsm_config_description, cfg_pytsm_config_id) VALUES ('loglevel_polld', 'DEBUG', 'NOTSET, ERROR, WARN, INFO, DEBUG, CRITICAL', 4);