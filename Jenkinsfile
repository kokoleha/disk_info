pipeline {
  agent { docker { image 'python:latest'} }
  stages {
    stage('build') {
      steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install psutil'
                    sh 'setsid python diskinfo.py'
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
