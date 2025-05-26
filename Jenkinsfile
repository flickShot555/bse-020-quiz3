pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Pulls the source code from the current branch
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                // Optionally display Python version
                sh 'python3 --version'
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the Python file
                sh 'python3 MyPython.py'
            }
        }
    }
}
