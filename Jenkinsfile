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
