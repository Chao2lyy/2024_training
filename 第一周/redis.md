##  Redis学习笔记


+ 键值存储：Redis是基于键值对的存储系统，每个键都对应一个值。
+ 数据类型：Redis支持多种数据类型，如字符串（String）、哈希（Hash）、列表（List）、集合（Set）、有序集合（Sorted Set）等。
+ 持久化：Redis支持将内存中的数据持久化到磁盘，确保数据在重启后不丢失。
+ 主从复制：Redis支持主从复制机制，可以创建多个节点实现数据的复制和高可用性。

### Redis 的基本操作
##### 安装和配置 Redis

在Ubuntu上安装Redis：

```bash

sudo apt-get update
sudo apt-get install redis-server
```
启动Redis服务：

```bash

sudo systemctl start redis
```
##### 使用 Redis 基本命令

连接Redis客户端：

```bash

redis-cli
```
设置和获取键值：

```bash

SET mykey "Hello Redis"
GET mykey
```
操作字符串类型：

```bash

SET counter 10
INCR counter
```
操作哈希类型：

```bash

HSET user:id:1 username john_doe
HGET user:id:1 username
```
操作列表类型：

```bash

LPUSH mylist "item1"
RPUSH mylist "item2"
LRANGE mylist 0 -1
```
操作集合类型：

```bash

SADD myset "member1"
SADD myset "member2"
SMEMBERS myset
```
操作有序集合类型：

```bash

ZADD leaderboard 1000 "player1"
ZADD leaderboard 900 "player2"
ZREVRANGE leaderboard 0 -1 WITHSCORES
```
##### 数据持久化和配置

持久化选项：

Redis支持两种持久化方式：RDB（快照）和AOF（日志）。

配置文件：

Redis的主要配置文件位于 /etc/redis/redis.conf，可以修改端口、内存限制、持久化设置等。
### Redis 进阶操作
##### 主从复制配置

配置主节点：

```bash

# redis.conf 配置
bind 127.0.0.1
port 6379
```
配置从节点：

```bash

# redis.conf 配置
bind 127.0.0.1
port 6380
replicaof 127.0.0.1 6379
```
##### 数据备份和恢复

手动备份和恢复：

```bash

# 备份数据
sudo cp /var/lib/redis/dump.rdb /path/to/backup/directory

# 恢复数据
sudo cp /path/to/backup/dump.rdb /var/lib/redis/
```
##### Redis 高级特性

事务：

```bash

MULTI
SET key1 "value1"
SET key2 "value2"
EXEC
```
发布与订阅：

```bash

# 发布消息
PUBLISH channel1 "Hello Subscribers"

# 订阅消息
SUBSCRIBE channel1
```