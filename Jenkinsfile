pipeline {
    agent any
    environment {
    GITHUB_CREDENTIALS = credentials('cd77a5bd-68e4-460e-a048-33076988332f')
    }
    stages {
        stage('Clone repository') {
      steps {
        git branch: 'main', credentialsId: env.GITHUB_CREDENTIALS, url: 'https://github.com/SalvaVamsiKasyap/orange_hrm.git'
      }
    }
        stage('Checkout') {
            steps {
                // Checkout the code from Git repository
                git branch: 'main', url: 'https://github.com/SalvaVamsiKasyap/orange_hrm.git'
                
            }
        }
        stage('Setup') {
            steps {
                // Install the required dependencies
                bat 'pip install -r requirements.txt'
                //bat 'git clone https://github.com/SalvaVamsiKasyap/orange_hrm.git'
            }
        }
        stage('Run Tests') {
            steps {
                   // Run the Pytest command
                   bat 'dir'
                   //bat 'git init'       
                   //dir('/ptests') {
                    // Run the Pytest command
                    //bat 'git init'
                    //bat 'pytest'
                    //bat 'pytest -k unsuc --html=report.html'
                }
              }
         }
    }
}
