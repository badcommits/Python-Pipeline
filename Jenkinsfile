pipeline {
     agent {
          docker { image 'python:latest' }
     }

     stages {
          stage('Git Checkout') {
               steps {
                    git branch: 'main', credentialsId: 'github', url: 'https://github.com/badcommits/Python-Pipeline.git'
               }
          }

          stage('Build') {
               steps {
                    echo 'Building Dependencies'
                    
               }
          }

          stage('Unit Testing') {
               steps {
                    
               }
          }

          stage('SonarQube Analysis') {
               steps {
                    
               }
          }

     }
}