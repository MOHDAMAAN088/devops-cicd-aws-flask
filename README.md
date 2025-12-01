🚀 DevOps CI/CD Pipeline with Docker & AWS Deployment (GitHub Actions)

This project demonstrates a complete DevOps workflow using:

GitHub Actions → Docker → AWS EC2 → Nginx → Automatic Deployment (SSH)

Whenever code is pushed to the main branch, the pipeline:

1️⃣ Builds Docker Image
2️⃣ Pushes Image to Docker Hub
3️⃣ SSH into AWS EC2
4️⃣ Pulls Latest Image & Deploys Container
5️⃣ App becomes live automatically via Nginx Reverse Proxy
