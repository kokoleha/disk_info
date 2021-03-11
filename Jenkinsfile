pipeline {
  agent { docker { image 'python:latest' } }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install --user -r pip-requirements.txt'
      }
    }
    stage('test') {
      steps {
        echo 'hello'
      }   
    }
  }
}
