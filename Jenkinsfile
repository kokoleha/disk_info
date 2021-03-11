pipeline {
  agent { docker { image 'python:latest'} }
  stages {
    stage('build') {
      steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install psutil'
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
