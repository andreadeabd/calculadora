pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/andreadeabd/calculadora'
                }
            }
        }
        stage('Verificar Python y pip') {
            steps {
                script {
                    // Verificar versión de Python y pip
                    sh 'python3 --version'
                    sh 'pip3 --version'
                }
            }
        }
        stage('Instalar Dependencias') {
            steps {
                script {
                    // Intentar instalar las dependencias sin crear un entorno virtual
                    sh 'pip3 install -r requirements.txt --user'
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Ejecutar pruebas
                    sh 'python3 -m unittest test_calculadora.py'
                }
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
