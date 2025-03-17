pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                git 'https://github.com/andreadeabd/calculadora.git'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                sh 'python -m unittest test_calculadora.py'
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
