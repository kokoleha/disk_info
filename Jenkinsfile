pipeline {
  agent { docker { image 'python:3.7' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install psutil'
      }
    }
    stage('test') {
      steps {
        echo 'hello'
      }   
    }
  }
}
