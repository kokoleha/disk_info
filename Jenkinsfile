pipeline {
    agent { docker {
            image 'python:latest'
            args '-p 8000:8000'
                   }
          }

    stages {
        stage('Main Stage') {
            parallel {
                stage('Stage 1: Run the diskinfo') {
                    steps { withEnv(["HOME=${env.WORKSPACE}"]) {
                            sh 'pip3 install psutil'
                            sh 'python diskinfo.py' }      
                          }
                }
                stage('Stage 2: first test') {
                    steps { withEnv(["HOME=${env.WORKSPACE}"]) {
                            sleep 30
                            sh 'pip3 install requests'
                            sh 'python test.py' }      
                          }
                }
                stage('Stage 3: second test') {
                    steps { sleep 35
                            echo 'The second test may be here' }
                }
            }
        }
    }
}
