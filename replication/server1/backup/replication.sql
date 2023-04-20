stop slave;
CHANGE MASTER TO MASTER_HOST = 'mysql2', MASTER_USER = 'replicator',
    MASTER_PASSWORD = 'repl1234or', MASTER_LOG_FILE = 'binlog.000002',
    MASTER_LOG_POS = 854;
start slave;
show slave status\g