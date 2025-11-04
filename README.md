# CI/CD Pipeline with Docker, GitHub, and Jenkins

## 🧩 Overview

This project demonstrates a **Continuous Integration and Continuous Deployment (CI/CD)** pipeline using **GitHub, Jenkins, and Docker**. The goal is to automate the process of building, testing, and deploying a containerized web application whenever code is pushed to GitHub.

---

## 📁 Project Structure

```
├── app.py              # Flask/Node.js app
├── requirements.txt     # Dependencies (if Flask app)
├── Dockerfile           # Docker build instructions
├── Jenkinsfile (optional)
└── README.md
```

---

## ⚙️ Part 1 — Jenkins Setup

### 1️⃣ Install Jenkins and Docker

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins docker.io -y
sudo systemctl enable jenkins --now
```

---

### 2️⃣ Give Jenkins Docker Permissions

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

> If permission errors persist:

```bash
sudo chmod 666 /var/run/docker.sock
```

---

### 3️⃣ Configure Jenkins

* Open Jenkins: `http://localhost:8080`
* Unlock Jenkins using the initial admin password.
* Install **Suggested Plugins**.
* Create your **admin user**.
* Install plugins:

  * **Git Plugin**
  * **Docker Pipeline**
  * **GitHub Integration**

---

## ⚙️ Part 2 — GitHub Integration

### 1️⃣ Create a GitHub Repository

Push your project (Flask/Node.js app + Dockerfile) to GitHub.

Example structure:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

### 2️⃣ Add Webhook for Jenkins

* Go to your GitHub repo → **Settings → Webhooks → Add Webhook**
* Payload URL: `https://<your-ngrok-url>/github-webhook/`
* Content type: `application/json`
* Trigger: **Just the push event**
* Save.

---

## ⚙️ Part 3 — Configure Jenkins Job

### 1️⃣ Create a New Freestyle Project

* Name: `CI-CD-Docker-App`
* Source Code Management: **Git**

  * Repository URL: `https://github.com/<username>/<repo>.git`
  * Branch: `*/main`
* Build Triggers: **GitHub hook trigger for GITScm polling**
* Build Environment: Check **Use secret text(s) or file(s)** if using credentials.

### 2️⃣ Build Steps

Add an **Execute Shell** build step:

```bash
echo "=== Building Docker Image ==="
docker build -t yourdockerhubusername/yourapp:latest .

echo "=== Running Container for Testing ==="
docker run -d -p 5000:5000 yourdockerhubusername/yourapp:latest
sleep 5
echo "Container running successfully!"

echo "=== Pushing to Docker Hub ==="
docker login -u yourdockerhubusername -p your_docker_pat
docker push yourdockerhubusername/yourapp:latest
```

---

## ⚙️ Part 4 — Ngrok for Webhooks

If Jenkins runs on localhost, expose it publicly using Ngrok:

```bash
cd D:\ngrok
./ngrok.exe http 8080
```

Copy the **Forwarding URL** (e.g., `https://random.ngrok.io`) and use it in your GitHub webhook.

---

## 🧪 Verification Steps

1. Make a small code change and push to GitHub.
2. Jenkins automatically builds the job.
3. The Docker image is built, tested, and pushed to Docker Hub.
4. (Optional) Add a deploy stage to a remote server.

---

## 🧰 Common Errors & Fixes

| Error                                               | Cause                       | Fix                                      |
| --------------------------------------------------- | --------------------------- | ---------------------------------------- |
| `permission denied while connecting to docker.sock` | Jenkins lacks Docker access | `sudo usermod -aG docker jenkins`        |
| `Couldn't find any revision to build`               | Wrong branch                | Set branch to `*/main`                   |
| `ngrok not recognized`                              | Not added to path           | Run from extracted folder or add to PATH |

---

## 🚀 Outcome

✅ Jenkins automatically builds and tests Docker image.
✅ GitHub Webhook triggers CI pipeline.
✅ Docker image pushed to Docker Hub.
✅ End-to-end CI/CD workflow achieved!

---

## 📜 Credits

Author: **Ansh Goyal**
Guide: CI/CD Assignment — Integrating **Docker**, **GitHub**, and **Jenkins**.
