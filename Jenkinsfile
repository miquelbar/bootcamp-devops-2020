def dockerImage
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("miquelbar/code:${env.BRANCH_NAME}-${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            when {
                expression { env.BRANCH_NAME != 'master' }
            }
            steps {
                script {
                    sh "make test"
                }
            }
        }
        stage('Deploy') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                echo 'Deploying....'
                script {
                    docker.withRegistry('https://repo.treescale.com', 'canister') {
                        dockerImage.push()
                    }
                    sh "sed -i'' 's/{{BUILD_ID}}/${env.BRANCH_NAME}-${env.BUILD_ID}/g' kubernetes/deployment.yml"
                    sh "cat kubernetes/deployment.yml"
                    sh "kubectl apply -f kubernetes/"
                }
            }
        }
    }
}