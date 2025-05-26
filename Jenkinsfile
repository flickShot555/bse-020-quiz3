pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Compile Java Program') {
            steps {
                // Compile the Java file
                bat 'javac program.java'
            }
        }

        stage('Run Java Program') {
            steps {
                // Run with echo input using a here-document
                bat '''
                java program <<EOF
10
5
+
EOF
                '''
            }
        }
    }
}
