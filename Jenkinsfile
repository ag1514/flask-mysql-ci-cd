pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-cred')
        IMAGE_NAME = "ansh15/flask-mysql-ci-cd"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ag1514/flask-mysql-ci-cd.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                '''
            }
        }

        stage('Run Container for Testing') {
            steps {
                sh '''
                echo "Running container for test..."
                docker run -d -p 5000:5000 --name flask-test $IMAGE_NAME:$BUILD_NUMBER
                sleep 5
                docker ps -a
                docker stop flask-test
                docker rm flask-test
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh '''
                echo "Pushing image to Docker Hub..."
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push $IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }

        stage('Deploy (Optional)') {
            steps {
                sh '''
                echo "Deploying container..."
                docker run -d -p 5000:5000 --name flask-app-latest $IMAGE_NAME:$BUILD_NUMBER || true
                '''
            }
        }
    }
}

