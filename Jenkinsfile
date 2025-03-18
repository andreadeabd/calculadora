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
