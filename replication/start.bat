docker run --name mysql1 ^
  -e MYSQL_ROOT_PASSWORD=mysql1pass ^
  -e MYSQL_DATABASE=mydata ^
  -e MYSQL_USER=master1 ^
  -e MYSQL_PASSWORD=cattle ^
  -dit -p 33061:3306 ^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server1\conf.d":/etc/mysql/mysql.conf.d ^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server1\data":/var/lib/mysql ^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server1\log":/var/log/mysql ^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server1\backup":/backup ^
  -h  mysql1 mysql

pause

docker run --name mysql2 ^
  --link mysql1 ^
  -e MYSQL_ROOT_PASSWORD=mysql2pass ^
  -e MYSQL_DATABASE=mydata ^
  -dit -p 33062:3306 ^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server2\conf.d":/etc/mysql/mysql.conf.d^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server2\data":/var/lib/mysql ^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server2\log":/var/log/mysql ^
  -v "C:\Users\Vladyslav Synytsyn\OneDrive\Documents\IdeaProjects\DistributedInformSystems\replication\server2\backup":/backup ^
  -h mysql2 mysql

docker exec -i mysql1 sh -c "echo '"172.17.0.3" mysql2 mysql2' >> /etc/hosts"