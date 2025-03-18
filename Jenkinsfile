pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                checkout scm: [
                    $class: 'GitSCM',
                    branches: [[name: 'refs/heads/main']],
                    userRemoteConfigs: [[url: 'https://github.com/andreadeabd/calculadora.git']]
                ]
            }
        }
        stage('Crear Entorno Virtual y Instalar Dependencias') {
            steps {
                script {
                    // Crear un entorno virtual
                    sh 'python3 -m venv venv'
                    // Activar el entorno virtual y luego instalar las dependencias
                    sh '''
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Ejecutar pruebas en el entorno virtual
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
