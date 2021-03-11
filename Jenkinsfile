pipeline {
  agent { docker { image 'python:latest, , args:'-u root:root'' } }
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                   
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
