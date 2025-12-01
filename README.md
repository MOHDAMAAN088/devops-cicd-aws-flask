📌 About the Project

This DevOps project demonstrates the complete automation of building, packaging, and deploying a Flask web application using CI/CD, Docker, and AWS EC2.
Whenever the developer pushes code to the main branch, GitHub Actions automatically:

✔ Builds a Docker image
✔ Pushes it to Docker Hub
✔ Connects to AWS EC2 via SSH
✔ Pulls and runs the latest container
✔ Serves live using Nginx reverse proxy
