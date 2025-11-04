Flask-MySQL CI/CD Pipeline using Jenkins, GitHub & Docker

This project demonstrates a complete CI/CD pipeline that automatically builds, tests, and deploys a Flask + MySQL application using Jenkins, GitHub Webhooks, Docker, and ngrok for local tunneling.

PROJECT OVERVIEW

Whenever a new commit is pushed to the GitHub repository:

GitHub Webhook sends a trigger to Jenkins (via ngrok URL).

Jenkins automatically pulls the latest code.

Docker builds a new image of the Flask app and runs it in a container.

Optionally, Jenkins can push this image to Docker Hub.

TECH STACK

GitHub – Source code & webhook trigger

Jenkins – Automation server for CI/CD

ngrok – Secure tunnel from localhost to the web

Docker – Containerization of Flask + MySQL app

Flask – Python web framework

MySQL – Backend database for the app

STEP 1: SETUP JENKINS

Download and install Jenkins from the official Jenkins website.
Run Jenkins on http://localhost:8080
Install these plugins: Git, Docker, and GitHub Integration
