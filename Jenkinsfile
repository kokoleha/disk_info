pipeline {
  agent { docker { image 'python:latest', args:'-u root:root' } }
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
