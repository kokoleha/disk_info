pipeline {
  agent { 
    checkout scm
    docker.image('python:latest').withRun('-p 8000:8000')
  }
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install psutil'
                    sh 'python diskinfo.py &'
                }                     
      }
    }
    stage('test') {
      steps {
        echo 'hello'
      }   
    }
  }
}
