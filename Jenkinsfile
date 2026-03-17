pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning the code from GitHub...'
                git url: 'https://github.com/chanhengmenh/devops-assignement-3.git', branch: 'main'
                echo 'Cloning Done'
            }
        }

        stage('Copy') {
            steps {
                echo 'Copying files to /home/ubuntu/current...'
                sh 'cp -r FoodExpressAPI /home/ubuntu/current'
                echo 'Copy Done'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t foodexpress/fastapi:v1.0 /home/ubuntu/current/FoodExpressAPI'
                echo 'Build Done'
            }
        }

        stage('Run Image As Container') {
            steps {
                echo 'Deploying container...'
                sh '''
                    docker stop foodexpress-container || true
                    docker rm foodexpress-container || true
                    docker run --name foodexpress-container -d -p 8000:8000 foodexpress/fastapi:v1.0
                '''
                echo 'FoodExpress FastAPI is running inside Docker on port 8000'
            }
        }

    }

    post {
        failure {
            echo 'Pipeline failed. Check the Console Output for details.'
        }
        success {
            echo 'Deployment Successful! FoodExpress APIs are live.'
        }
    }
}
