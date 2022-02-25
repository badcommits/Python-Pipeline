pipeline {
     agent any

     stages {
          stage('Git Checkout') {
               steps {
                    git branch: 'main', credentialsId: 'github', url: 'https://github.com/badcommits/Python-Pipeline.git'
               }
          }

          stage('Build') {
               steps {
                    echo 'Building Dependencies'
                    sh 'apt update'
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