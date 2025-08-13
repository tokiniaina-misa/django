pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t djangochat:latest .'
            }
        }

        stage('Run Container') {
            steps {
                script {
                    try {
                        // Lancer le container en mode détaché
                        sh 'docker run -d -p 5000:5000 --name djangochat_container djangochat:latest'
                        
                        // Afficher les logs pour vérification
                        sh 'docker logs djangochat_container'
                        
                    } catch (err) {
                        error("Échec du démarrage du container: ${err}")
                    }
                }
            }
        }
    }

    post {
        failure {
            echo 'Échec - Nettoyage des containers...'
            sh 'docker rm -f djangochat_container || true'
            sh 'rm -f db.sqlite3 || true'
        }
        success {
            echo 'Succès - Le conteneur reste en marche'
        }
    }
}
