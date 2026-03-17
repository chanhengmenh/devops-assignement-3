# FoodExpress API — DevOps Assignment 3 In Professor Chandun Class 😁😁

A FastAPI-based food ordering REST API with a fully automated CI/CD pipeline using Jenkins and Docker, deployed on AWS EC2.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [API Endpoints](#api-endpoints)
- [Running Locally](#running-locally)
- [Docker](#docker)
- [Jenkins CI/CD Pipeline](#jenkins-cicd-pipeline)
- [AWS EC2 Setup](#aws-ec2-setup)

---

## Project Structure

```
devops-assignement-3/
├── FoodExpressAPI/
│   ├── main.py           # FastAPI application (CRUD for /orders)
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        # Container definition
└── Jenkinsfile           # 4-stage Jenkins pipeline
```

---

## Tech Stack

| Layer     | Technology       |
| --------- | ---------------- |
| Language  | Python 3.11      |
| Framework | FastAPI          |
| Server    | Uvicorn          |
| Container | Docker           |
| CI/CD     | Jenkins          |
| Cloud     | AWS EC2 (Ubuntu) |

---

## API Endpoints

Base URL (local): `http://127.0.0.1:8000`
Base URL (EC2):   `http://<EC2_PUBLIC_IP>:8000`

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/`            | Welcome message          |
| GET    | `/health`      | Health check             |
| GET    | `/orders`      | List all orders          |
| GET    | `/orders/{id}` | Get a single order by ID |
| POST   | `/orders`      | Create a new order       |
| PUT    | `/orders/{id}` | Update an existing order |
| DELETE | `/orders/{id}` | Delete an order          |

### Order Schema

```json
{
  "customer": "Alice",
  "item": "Burger",
  "quantity": 2,
  "status": "pending"
}
```

`status` defaults to `"pending"` if not provided. All fields except `status` are required on creation; all fields are optional on update.

### Example Requests

**Create an order**

```bash
curl -X POST http://127.0.0.1:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"customer": "Alice", "item": "Burger", "quantity": 2}'
```

**Update an order**

```bash
curl -X PUT http://127.0.0.1:8000/orders/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "delivered"}'
```

**Delete an order**

```bash
curl -X DELETE http://127.0.0.1:8000/orders/1
```

---

## Running Locally

**Prerequisites:** Python 3.11+

```bash
cd FoodExpressAPI
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive docs (Swagger UI) are available at `http://127.0.0.1:8000/docs`.

---

## Docker

**Build the image**

```bash
cd FoodExpressAPI
docker build -t foodexpress/fastapi:v1.0 .
```

**Run the container**

```bash
docker run --name foodexpress-container -d -p 8000:8000 foodexpress/fastapi:v1.0
```

**Stop and remove the container**

```bash
docker stop foodexpress-container
docker rm foodexpress-container
```

The Dockerfile uses `python:3.11-slim`, exposes port `8000`, and starts Uvicorn bound to `0.0.0.0`.

---

## Jenkins CI/CD Pipeline

The `Jenkinsfile` defines a 4-stage pipeline:

| Stage                            | Description                                                                |
| -------------------------------- | -------------------------------------------------------------------------- |
| **Clone**                  | Pulls the latest code from the GitHub repository (`main` branch)         |
| **Copy**                   | Copies `FoodExpressAPI/` to `/home/ubuntu/current` on the EC2 instance |
| **Build Docker Image**     | Builds `foodexpress/fastapi:v1.0` from the copied files                  |
| **Run Image As Container** | Stops any existing container and starts a fresh one on port `8000`       |

Post-build notifications are printed to the console for both success and failure.

### Before Pushing

Update these values in `Jenkinsfile` to match your setup:

- **Line 9** — replace the `git url` with your own GitHub repository URL.

---

## AWS EC2 Setup

**Required Security Group inbound rules:**

| Port | Purpose        |
| ---- | -------------- |
| 22   | SSH access     |
| 8080 | Jenkins Web UI |
| 8000 | FastAPI app    |

**Recommended EC2 instance:** Ubuntu 22.04 LTS, `t2.micro` or larger.

After Jenkins deploys the pipeline successfully, the API is accessible at:

```
http://<EC2_PUBLIC_IP>:8000
```
