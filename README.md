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

# ✅ Start and Stop the Application using compose

### What is Docker Compose?
Docker Compose is a tool that lets you define and run multi‑container Docker applications using a single configuration file (typically **docker‑compose.yml**) instead of many individual docker run commands.


**📄 How it works**
You define:
- **Services** — each container part of your app (e.g., database, API, frontend)
- **Networks** — how services connect
- **Volumes** — persistent storage for containers

```bash
docker compose up --build -d
```

*Builds and starts all services defined in the `docker-compose.yml` file in detached mode.*

```bash
docker compose down
```

*Stops and removes all containers and networks created by the `up` command.*

  > By default, this command stops and deletes the containers and networks created by `docker compose up`, but does **not** delete named volumes unless the `-v` flag is also used.
