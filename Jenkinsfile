pipeline {
  agent { 
docker { image 'python:latest'}
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
}
