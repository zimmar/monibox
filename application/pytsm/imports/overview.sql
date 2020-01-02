INSERT INTO cfg_pytsm_overview
    (
     cfg_pytsm_overview_id,
     cfg_pytsm_base_name,
     cfg_pytsm_base_label,
     cfg_pytsm_base_sortorder,
     cfg_pytsm_base_alert_cmp,
     cfg_pytsm_base_alert_val,
     cfg_pytsm_base_alert_col,
     cfg_pytsm_overview_query,
     cfg_pytsm_overview_unit,
     cfg_pytsm_overview_notforlibclient,
     cfg_pytsm_overview_pollfreq,
     cfg_pytsm_overview_parent_id)
VALUES
(1, 'total_data_stored', 'C__PYTSM_TOTAL_DATA_STORED', 10, null, null, null, 'SELECT CAST(FLOAT(SUM(logical_mb)) / 1024 / 1024 AS DEC(8,3)) FROM occupancy', 'TB', 0, 3, 3),
(2, 'total_data_backuped', 'C__PYTSM_TOTAL_DATA_BACKUPED', 20, null, null, null, 'select ''''N/A'''' from status', 'TB', 0, 3, 3),
(3, 'total_data_archived', 'C__PYTSM_TOTAL_DATA_ARCHIVED', 30, null, null, null, 'select ''''N/A'''' from status', 'TB', 0, 3, 3),

(4, 'scratch_tapes', 'C__PYTSM_HEALTH_DATA_SCRATCH_TAPES', 10, 'less', '10', 'alarm', '''SELECT COUNT(*) FROM libvolumes WHERE status=''Scratch''', '', 1, 3, 1),
(5, 'volumes_with_errors', 'C__PYTSM_HEALTH_DATA_VOLUMES_WITH_ERRORS', 20, 'more', '0', 'alarm', '''SELECT COUNT(*) FROM volumes WHERE error_state=''YES''', '', 0, 3, 1),
(6, 'unavailable_volumes', 'C__PYTSM_HEALTH_DATA_UNAVAILABLE_VOLUMES', 30, 'more', '0', 'alarm', '''SELECT COUNT(*) FROM volumes WHERE access=''UNAVAILABLE''', '', 0, 3, 1),
(7, 'drives_offline', 'C__PYTSM_HEALTH_DATA_DRIVES_OFFLINE', 40, 'more', '0', 'alarm', 'SELECT COUNT(*) FROM drives WHERE NOT online=''YES''', '', 1, 3, 1),
(8, 'paths_offline', 'C__PYTSM_HEALTH_DATA_PATHS_OFFLINE', 50, 'more', '0', 'alarm', 'SELECT COUNT(*) FROM paths WHERE NOT online=''YES''', '', 1, 3, 1),

(9, 'cache_hit', 'C__PYTSM_DATABASE_CHACHE_HIT', 10, 'less', '98.0', 'warn','SELECT BUFF_HIT_RATIO from db', '%', 0, 3, 2),
(10, 'database_usage','C__PYTSM_DATABASE_USAGE', 20, 'more', '90.0', 'alarm', 'select used_db_space_mb*100/free_space_mb from db', '%',  0, 3, 2),
(11, 'log_usage', 'C__PYTSM_DATABASE_LOG_USAGE', 30, 'more', '90.0', 'alarm','select used_space_mb*100/free_space_mb from log', '%',  0, 3, 2),
(12, 'db_fragmentation', 'C__PYTSM_DATABASE_DB_FRAGMENTATION', 40, 'more', '10.0', 'alarm', 'select ''N/A'' from status', '%',  0, 3, 2),
(13, 'db_volumes_not_synced', 'C__PYTSM_DB_VOLUMES_NOT_SYNCED', 50, 'more', '0', 'alarm', 'select ''N/A'' from status', '',  0, 3, 2),
(14, 'db_logs_not_synced', 'C__PYTSM_DATABASE_LOG_NOT_SYNCED', 60, 'more', '0', 'alarm', 'select ''N/A'' from status', '', 0, 3, 2),
(15, 'last_db_backup', 'C__PYTSM_DB_BACKUP', 70, null, null, null, 'SELECT last_backup_date FROM db',  '', 0, 3, 2),

(16, 'Failed Admin Schedules', 'C__PYTSM_SCHEDULES_FAILED_ADMIN' , 10, 'more', '0', 'alarm', 'SELECT count(*) FROM events WHERE status <> ''Completed'' AND status <> ''Future'' AND status <> ''Started'' AND status <> ''Restarted'' and status <> ''In Progres'' and status <> ''Pending'' AND NODE_NAME is NOT NULL', '', 0, 3, 4),
(17, 'Failed Client Schedules', 'C__PYTSM_SCHEDULES_FAILED_CLIENT', 20, 'more', '0', 'alarm', 'SELECT count(*) FROM events WHERE status NOTEQUAL ''Completed'' AND status NOTEQUAL ''Future'' AND status NOTEQUAL ''Started'' AND status NOTEQUAL ''Restarted'' and status NOTEQUAL ''In Progres'' and status NOTEQUAL ''Pending'' AND NODE_NAME is NOT NULL', '', 0, 3, 4),
(18, 'Running Client Schedules', 'C__PYTSM_SCHEDULES_RUNNING_CLIENT', 30, 'more', '0', 'warn', 'SELECT count(*) FROM events WHERE status <> ''Completed'' AND status <> ''Future'' AND (status=''In Progres'' OR status=''Started'' OR status=''Restarted'') and NODE_NAME is NOT NULL', '', 0, 3, 4),
(19, 'Running Admin Schedules', 'C__PYTSM_SCHEDULES_RUNNING_ADMIN', 40, 'more', '0', 'warn', 'SELECT count(*) FROM events WHERE status <> ''Completed'' AND status <> ''Future'' AND (status=''In Progre%'' OR status=''Started'' OR status=''Restarted'') and NODE_NAME is NULL', '', 0, 3, 4);
