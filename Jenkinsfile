pipeline {
  agent { docker { image 'python:latest'} }
  stages {
    stage('build') {
      steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install psutil'
                }      
                sh 'python diskinfo.py'
      }
    }
    stage('test') {
      steps {
        echo 'hello'
      }   
    }
  }
}
