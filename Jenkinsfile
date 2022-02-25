pipeline {
     agent {
          docker {
            image 'python:latest'
            args '-u root'
        }
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
                    sh 'pip install -r requirements.txt'
                    
               }
          }

          stage('Unit Testing') {
               steps {
                    echo 'Unit Testing'
               }
          }

          stage('SonarQube Analysis') {
               steps {
                    echo 'SonarQube testing'     
               }
          }

     }
}