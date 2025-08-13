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
                        // Lancer le container en mode détaché pour pouvoir continuer
                        sh 'docker run -d -p 5000:5000 --name djangochat_container djangochat:latest'
                        // Attendre que le container soit prêt (ajuster le sleep si nécessaire)
                        sleep 10
                        // Vérifier les logs (c'est 'docker logs' avec un 's' à la fin)
                        sh 'docker logs djangochat_container'
                        // Exemple de test - remplacer par votre commande de test réelle
                        sh 'curl --fail http://localhost:5000 || exit 1'
                    } catch (err) {
                        error("Tests failed: ${err}")
                    } finally {
                        // Arrêter le container même en cas d'échec
                        sh 'docker stop djangochat_container || true'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Nettoyage des containers et de la base SQLite...'
            sh 'docker rm -f djangochat_container || true'
            sh 'rm -f db.sqlite3 || true'
        }
        failure {
            echo 'Tests échoués — Tout a été nettoyé.'
        }
        success {
            echo 'Tests réussis'
        }
    }
}
