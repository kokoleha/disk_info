pipeline {
  agent { docker { image 'python:latest' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r pip-requirements.txt'
      }
    }
    stage('test') {
      steps {
        echo 'hello'
      }   
    }
  }
}
