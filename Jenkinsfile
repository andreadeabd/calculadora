pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                script {
                    // Clonamos el repositorio y nos aseguramos de estar en la rama main
                    git 'https://github.com/tuusuario/calculadora_project.git'
                    sh 'git checkout main'
                }
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                sh 'python3 -m unittest test_calculadora.py'
            }
        }
    }

    post {
        success {
            echo '¡Pruebas exitosas!'
        }
        failure {
            echo 'Las pruebas fallaron.'
        }
    }
}
