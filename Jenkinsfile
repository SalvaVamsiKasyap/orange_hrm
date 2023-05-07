pipeline {
    agent any
    environment {
    GITHUB_CREDENTIALS = credentials('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')
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
                bat 'dir'
                dir('/ptests'){
                    bat 'dir'
                }
            }
        }
        //stage('Setup') {
            //steps {
                // Install the required dependencies
                //bat 'pip install -r requirements.txt'
                //bat 'git clone https://github.com/SalvaVamsiKasyap/orange_hrm.git'
            //}
        //}
        //stage('Run Tests') {
            //steps {
                   // Run the Pytest command
                   //bat 'dir'
                   //bat 'git init'       
                   //dir('/ptests') {
                    // Run the Pytest command
                    //bat 'dir'
                    //bat 'pytest -k unsuc --html=report.html'
                //}
              //}
         //}
    }
}
