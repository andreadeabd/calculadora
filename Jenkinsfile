pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                script {
                    // Clonar el repositorio desde GitHub
                    git branch: 'main', url: 'https://github.com/andreadeabd/calculadora'
                }
            }
        }
        stage('Verificar Python y pip') {
            steps {
                script {
                    // Verificar versiones de Python y pip
                    sh 'python3 --version'
                    sh 'pip3 --version'
                }
            }
        }
        stage('Crear Entorno Virtual y Instalar Dependencias') {
            steps {
                script {
                    // Instalar dependencias con pipx
                    sh 'pipx install -r requirements.txt'
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Ejecutar pruebas dentro del entorno virtual
                    sh '. venv/bin/activate && python3 -m unittest test_calculadora.py'
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
