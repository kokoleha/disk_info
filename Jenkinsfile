pipeline {
    agent { docker { image 'python:latest'} }
    stages {
        stage('Example Stage') {
            parallel {
                stage('Stage 1') {
                    steps { withEnv(["HOME=${env.WORKSPACE}"]) {
                            sh 'pip3 install psutil'
                            sh 'python diskinfo.py' }      
                          }
                }
                stage('Stage 2') {
                    steps { sh 'echo stage 2 passed' }
                }
                stage('Stage 3') {
                    steps { sh 'echo stage 3 passed' }
                }
            }
        }
    }
}
