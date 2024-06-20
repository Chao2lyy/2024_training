## Linux/Shell 学习笔记
### Linux 简介与基础
#### Linux 内核与发行版

Linux是一个开源的类Unix操作系统内核，通过各种Linux发行版（如Ubuntu、CentOS、Debian等）来管理和发布。
#### 文件系统与路径操作

##### 文件系统层级结构：

Linux文件系统以树状结构组织，根目录为/，包含各种系统和用户目录。

##### 路径操作：

```bash

# 当前目录
pwd

# 列出目录内容
ls

# 切换目录
cd <目录路径>

# 创建目录
mkdir <目录名>

# 删除目录
rmdir <目录名>

# 复制文件或目录
cp <源路径> <目标路径>

# 移动或重命名文件或目录
mv <源路径> <目标路径>

# 删除文件或目录
rm <文件或目录名>
```
##### 用户和权限管理

###### 用户和组管理：

```bash

# 添加用户
sudo adduser <用户名>

# 删除用户
sudo deluser <用户名>

# 添加用户到组
sudo usermod -aG <组名> <用户名>

# 修改文件所有者
sudo chown <新所有者> <文件>

# 修改文件权限
sudo chmod <权限设置> <文件>
```
##### 系统管理和网络配置

###### 系统信息：

```bash

# 查看系统信息
uname -a

# 查看CPU信息
cat /proc/cpuinfo

# 查看内存信息
cat /proc/meminfo

# 查看网络接口信息
ifconfig
```
###### 网络配置：

```bash

# 查看路由表
route -n

# 设置静态IP地址
sudo nano /etc/network/interfaces
```

#### 基本语法和控制结构

##### 变量和数据类型：

```bash

# 定义变量
name="John"

# 输出变量值
echo "Hello, $name!"

# 数组定义和使用
fruits=("apple" "banana" "cherry")
echo "First fruit: ${fruits[0]}"

# 字符串操作
string="Hello World"
echo ${string:0:5}   # 输出 Hello
```
##### 条件判断和循环：

```bash

# if-else条件判断
if [ condition ]; then
    # 条件成立执行的命令
else
    # 否则执行的命令
fi

# for循环
for i in {1..5}; do
    echo "Iteration $i"
done

# while循环
counter=0
while [ $counter -lt 5 ]; do
    echo "Counter: $counter"
    ((counter++))
done
```

##### 函数和参数传递

###### 函数定义和调用：

```bash

# 定义函数
function greet() {
    echo "Hello, $1!"
}

# 调用函数
greet "Alice"
```

###### 命令行参数：

```bash

# $0 - 脚本名称
# $1, $2, ... - 第一个、第二个参数，依此类推
echo "Script name: $0"
echo "First argument: $1"
```
##### 文件操作和进程管理

###### 文件操作：

```bash

# 读取文件内容
cat <文件名>

# 追加内容到文件
echo "New line" >> <文件名>

# 判断文件是否存在
if [ -f <文件名> ]; then
    echo "File exists"
fi

# 文件遍历
for file in *; do
    echo "File: $file"
done
```
###### 进程管理：

```bash

# 列出所有进程
ps aux

# 查找特定进程
pgrep <进程名>

# 结束进程
kill <进程ID>
```
#### 高级应用场景与技术
##### 网络和安全管理

###### 防火墙设置：

```bash

# 查看防火墙状态
sudo ufw status

# 允许或拒绝端口访问
sudo ufw allow <端口号>
sudo ufw deny <端口号>
```
###### SSH远程连接：

```bash

# 安装SSH服务器
sudo apt-get install openssh-server

# 启动SSH服务
sudo service ssh start

# 远程连接到服务器
ssh username@hostname
```

##### 数据库和Web服务管理

###### 数据库操作：

```bash

# 安装MySQL数据库
sudo apt-get install mysql-server

# 登录MySQL
mysql -u root -p

# 创建数据库和用户
CREATE DATABASE mydb;
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mydb.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
```
###### Web服务设置：

```bash

# 安装Apache Web服务器
sudo apt-get install apache2

# 启动Apache服务
sudo systemctl start apache2

# 配置虚拟主机和网站
sudo nano /etc/apache2/sites-available/mywebsite.conf
sudo a2ensite mywebsite.conf
sudo systemctl reload apache2
```