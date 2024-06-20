## Mysql
#### MySQL 的基本操作

##### 启动MySQL服务：

```bash

sudo systemctl start mysql
```

##### 登录 MySQL：

```bash

mysql -u <用户名> -p
```
##### 查看MySQL版本：

```sql

SELECT VERSION();
```
##### 创建数据库：

```sql

CREATE DATABASE mydatabase;
```
##### 使用数据库：

```sql

USE mydatabase;
```
##### 创建表：

```sql

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
##### 插入数据：

```sql

INSERT INTO users (username, email) VALUES ('john_doe', 'john@example.com');
```
##### 查询数据：

```sql

SELECT * FROM users;
```
##### 更新数据：

```sql

UPDATE users SET email = 'john.doe@example.com' WHERE id = 1;
```
##### 删除数据：

```sql

DELETE FROM users WHERE id = 1;
```
#### 数据库管理和用户权限

##### 管理数据库：

```sql

SHOW DATABASES;  -- 显示所有数据库
DROP DATABASE mydatabase;  -- 删除数据库
```
##### 管理用户和权限：

```sql

CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';  -- 创建用户
GRANT ALL PRIVILEGES ON mydatabase.* TO 'newuser'@'localhost';  -- 授予用户权限
FLUSH PRIVILEGES;  -- 刷新权限
```

#### MySQL 进阶操作
##### 数据查询和过滤
###### 条件查询：

```sql

SELECT * FROM users WHERE username = 'john_doe';
```
###### 排序和限制：

```sql

SELECT * FROM users ORDER BY id DESC LIMIT 10;
```
###### 聚合函数和分组：

```sql

SELECT COUNT(*) AS total_users FROM users;
SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department;
```
##### 数据表设计和优化

###### 索引设计：

```sql

CREATE INDEX idx_username ON users (username);
```
###### 优化查询：

```sql

EXPLAIN SELECT * FROM users WHERE username = 'john_doe';
```
###### 事务管理：

```sql

START TRANSACTION;  -- 开始事务
-- 执行一系列SQL语句
COMMIT;  -- 提交事务
ROLLBACK;  -- 回滚事务
```
##### 外键约束和触发器

###### 外键约束：

```sql

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```
###### 触发器：

```sql

DELIMITER //
CREATE TRIGGER before_insert_users
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    SET NEW.created_at = NOW();
END;
//
DELIMITER ;
```