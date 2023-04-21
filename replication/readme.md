1. Download image from docker  
   `docker pull mysql`
2. Start the containers  
   `.\start.bat`
3. Log in into containers and initialize them

   Server1:
   ```
   docker exec -ti mysql1 sh -c "mysql -uroot -p"
   source /backup/initdb.sql
   ```
   Server2:
   ```
   docker exec -ti mysql2 sh -c "mysql -uroot -p"
   SET GLOBAL server_id = 2;
   source /backup/initdb.sql
   ```
4. Using the filename and the position
   from the table from previous step, change the replication.sql files
   with the corresponding values. This files and position must be the same
   for all nodes.
   ```
   source /backup/replication.sql
   ```
   or  
   server2:
   ```
   stop slave;
   CHANGE MASTER TO MASTER_HOST = 'mysql1', MASTER_USER = 'replicator',
   MASTER_PASSWORD = 'repl1234or', MASTER_LOG_FILE = '<>',
   MASTER_LOG_POS = <>;
   start slave;
   show slave status\g
   ```
   server1:
   ```
   stop slave;
   CHANGE MASTER TO MASTER_HOST = 'mysql2', MASTER_USER = 'replicator',
   MASTER_PASSWORD = 'repl1234or', MASTER_LOG_FILE = '<>',
   MASTER_LOG_POS = <>;
   start slave;
   show slave status\g
   ```
5. Test the replication
   server1:
   ```
   use mydata;
   Create table students (id int, name varchar(20));
   ```
   server2:
   ```
   show tables in mydata;
   ```