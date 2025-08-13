pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t djangochat:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh 'docker run --name djangochat_container djangochat:latest'
                    } catch (err) {
                        error("Tests failed ")
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Nettoyage des containers et de la base SQLite...'
            sh 'docker rm -f djangochat_container || true'
            sh 'rm -f db.sqlite3'
        }
        failure {
            echo 'Tests échoués — Tout a été nettoyé.'
        }
        success {
            echo 'Tests réussis'
        }
    }
}
