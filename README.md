# Docker + Flask + MySQL Setup (with Persistent Volume)

## ✅ 1. Pull and Run MySQL with a Volume

```bash
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=admin \
  -v arvind-data:/var/lib/mysql \
  mysql:latest
```

## ✅ 2. Build Your Flask App Image

```bash
docker build -t my-app .
```

## ✅ 3. Create a Docker Network

```bash
docker network create arvind-network
```

## ✅ 4. Connect Containers to the Network

```bash
docker network connect arvind-network mysql
docker network connect arvind-network my-app
```

## ✅ 5. Inspect Network (Optional)

```bash
docker network inspect arvind-network
```

## ✅ 6. Enter MySQL and Create Database/Table

```bash
docker exec -it mysql mysql -u root -p
```

```bash
CREATE DATABASE flask_db;
USE flask_db;

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255) NOT NULL
);
```

## 🧪 Test Volume Persistence

Even if you remove the container, the data stays because of the volume.

## ✅ Stop & Remove the Old MySQL Container

```bash
docker stop mysql
docker rm mysql
```

## ✅ Recreate MySQL Using the Same Volume

```bash
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=admin \
  -v arvind-data:/var/lib/mysql \
  mysql:latest
```

## ✅ Reconnect to Network

```bash
docker network connect arvind-network mysql
```

### 🚀 Your Flask app continues working with the same database and data because the volume (arvind-data) keeps it persistent.
