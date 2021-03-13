    parallel firstBranch: {
        // do something
    }, secondBranch: {
        // do something else
    },
    failFast: true|false
pipeline {
  agent { 
    checkout scm
    docker.image('python:latest').withRun('-p 8000:8000')
  }
  parallel firstBranch: {
    stages {
      stage('build') {
        steps {
          withEnv(["HOME=${env.WORKSPACE}"]) {
                      sh 'pip3 install psutil'
                      sh 'python diskinfo.py &'
                  }                     
        }  
      }
    }, secondBranch: {
      stage('test') {
        steps {
          echo 'hello'
        }   
      }
  },
    failFast: true|false
}
