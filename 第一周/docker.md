## Docker 学习笔记
### Docker 简介与基础概念
#### 什么是Docker？

Docker是一种开源的容器化平台，用于开发、交付和运行应用程序。它允许开发者将应用程序及其依赖项打包成一个称为容器的轻量级、可移植的虚拟化环境，可以在任何环境中运行。
#### Docker 的核心概念

+ 镜像（Image）：容器的基础，包含运行应用程序所需的所有内容。
+ 容器（Container）：基于镜像创建的运行实例，包含应用程序及其运行时环境。
+ 仓库（Repository）：用于存储和分享镜像的地方，如Docker Hub。

### Docker 的基本操作
##### 安装 Docker

###### Linux上安装Docker：
https://www.runoob.com/docker/ubuntu-docker-install.html

##### 启动Docker服务：

```bash

sudo systemctl start docker
```

##### 使用 Docker 基本命令

###### 查看Docker版本：

```bash

docker --version
```
###### 查找可用的镜像：

```bash

docker search <镜像名称>
```
###### 拉取镜像到本地：

```bash

docker pull <镜像名称>:<标签>
```
###### 运行容器：

```bash

docker run -it <镜像名称> bash
```
###### 列出运行中的容器：

```bash

docker ps
```
###### 停止容器：

```bash

docker stop <容器ID>
```
###### 删除容器：

```bash

docker rm <容器ID>
```
##### 构建和发布自定义镜像

###### 编写 Dockerfile：

```dockerfile

# 基础镜像
FROM ubuntu:latest

# 维护者信息
LABEL maintainer="your_email@example.com"

# 安装应用程序或配置环境
RUN apt-get update && apt-get install -y \
    package1 \
    package2

# 设置工作目录
WORKDIR /app

# 暴露端口
EXPOSE 80

# 启动应用程序命令
CMD ["command_to_run"]
```
###### 构建镜像：

```bash

docker build -t <镜像名称>:<标签> .
```
###### 发布到Docker仓库：

```bash

docker login
docker push <镜像名称>:<标签>
```
### Docker 进阶操作
##### 网络和数据卷管理

###### 创建网络：

```bash

docker network create <网络名称>
```
###### 挂载数据卷：

```bash

docker volume create <卷名称>
```
##### Docker Compose

Docker Compose是一个工具，用于定义和运行多容器的Docker应用。通过一个YAML文件定义应用的服务、网络和卷。

###### 安装 Docker Compose：

```bash

sudo curl -L "https://github.com/docker/compose/releases/download/<版本号>/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
###### 使用 Docker Compose：

```yaml

# docker-compose.yml 示例
version: '3'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
```
###### 启动应用：

```bash

docker-compose up
```
###### 停止应用：

```bash

docker-compose down
```