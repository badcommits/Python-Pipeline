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
                    sh '''
                    coverage run -m unittest unit_test.py
                    coverage report -m
                    coverage xml
                    '''
               }
          }

          stage('SonarQube Analysis') {
               steps {
                    echo 'SonarQube testing'
                    def scannerHome = tool 'SonarScanner 4.0';
                    withSonarQubeEnv('My SonarQube Server') { // If you have configured more than one global server connection, you can specify its name
                         sh "${scannerHome}/bin/sonar-scanner"
                    }
               }

     }
}