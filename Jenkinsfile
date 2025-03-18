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
                script {
                    // Crear un entorno virtual
                    sh 'python3 -m venv venv'
                    // Activar el entorno virtual e instalar las dependencias
                    sh '''
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Activar el entorno virtual antes de ejecutar las pruebas
                    sh '''
                        source venv/bin/activate
                        python3 -m unittest test_calculadora.py
                    '''
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
