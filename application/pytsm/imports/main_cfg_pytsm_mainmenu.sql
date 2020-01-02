create table cfg_pytsm_mainmenu
(
    cfg_pytsm_mainmenu_id    integer     not null
        primary key autoincrement,
    cfg_pytsm_base_label     varchar(45) not null,
    cfg_pytsm_base_sortorder smallint    not null,
    cfg_pytsm_base_name      varchar(45) not null
        unique
);

INSERT INTO cfg_pytsm_mainmenu (cfg_pytsm_mainmenu_id, cfg_pytsm_base_label, cfg_pytsm_base_sortorder, cfg_pytsm_base_name) VALUES (1, 'LB_PYTSM_BASE_NODES', 10, 'CFG_PYTSM_BASE_NODES');
INSERT INTO cfg_pytsm_mainmenu (cfg_pytsm_mainmenu_id, cfg_pytsm_base_label, cfg_pytsm_base_sortorder, cfg_pytsm_base_name) VALUES (2, 'LB_PYTSM_BASE_SERVER', 20, 'CFG_PYTSM_BASE_SERVER');
INSERT INTO cfg_pytsm_mainmenu (cfg_pytsm_mainmenu_id, cfg_pytsm_base_label, cfg_pytsm_base_sortorder, cfg_pytsm_base_name) VALUES (3, 'LB_PYTSM_BASE_BACKUP_ARCHIVE', 30, 'CFG_PYTSM_BASE_BACKUP_ARCHIVE');
INSERT INTO cfg_pytsm_mainmenu (cfg_pytsm_mainmenu_id, cfg_pytsm_base_label, cfg_pytsm_base_sortorder, cfg_pytsm_base_name) VALUES (4, 'LB_PYTSM_BASE_SCHEDULES', 40, 'CFG_PYTSM_BASE_SCHEDULES');
INSERT INTO cfg_pytsm_mainmenu (cfg_pytsm_mainmenu_id, cfg_pytsm_base_label, cfg_pytsm_base_sortorder, cfg_pytsm_base_name) VALUES (5, 'LB_PYTSM_BASE_ACTIVITY', 50, 'CFG_PYTSM_BASE_ACTIVITY');
INSERT INTO cfg_pytsm_mainmenu (cfg_pytsm_mainmenu_id, cfg_pytsm_base_label, cfg_pytsm_base_sortorder, cfg_pytsm_base_name) VALUES (6, 'LB_PYTSM_BASE_SERVER_STORAGE', 60, 'CFG_PYTSM_BASE_SERVER_STORAGE');
INSERT INTO cfg_pytsm_mainmenu (cfg_pytsm_mainmenu_id, cfg_pytsm_base_label, cfg_pytsm_base_sortorder, cfg_pytsm_base_name) VALUES (7, 'LB_PYTSM_BASE_OFFSITE_MANAGEMENT', 70, 'CFG_PYTSM_BASE_OFFSITE_MANAGEMENT');