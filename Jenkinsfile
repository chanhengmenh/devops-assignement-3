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
