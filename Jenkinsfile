pipeline {
    agent any

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

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest || echo "No tests found"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask App...'
                sh '''
                . venv/bin/activate
                python app.py &
                '''
            }
        }
    }
}
