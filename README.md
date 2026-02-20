# infrastructure-docker

Collection of Dockerfiles and Docker Compose configurations for building and managing containerized infrastructure services.

## 📌 Overview
This repository provides a curated set of reusable Dockerfiles and Docker Compose templates designed to standardize and simplify the deployment of common infrastructure components used across development, testing, and production environments.

Each service is organized in its own directory, containing:
- A `Dockerfile` (when a custom image is required)
- One or more Compose configurations inside a `compose/` folder
- An optional `README.md` with service‑specific notes

The goal of this repository is to centralize infrastructure‑related container definitions, promote reusability, avoid duplicated configurations across projects, and maintain a clean structure for both standalone services and multi‑service stacks.

---

## 📁 Repository Structure
```
infrastructure-docker/
│
└── service-name/
    ├── Dockerfile
    ├── compose/
    │   └── docker-compose.yml
    └── README.md
```

---

## 🚀 Usage
### ▶️ Build a Docker image
```bash
docker build -t <image-name> .
```

### ▶️ Start a service using Docker Compose
```bash
docker compose -f compose/docker-compose.yml up -d
```

### ▶️ Stop a service
```bash
docker-compose down
```
