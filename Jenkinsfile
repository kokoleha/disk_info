pipeline {
  agent { docker { image 'python:latest'} }
  stages {
    stage('build') {
      steps {
        
                    parallel parallelTask1: {  //название паралельного выполнение чтобы различать в отчете
            	build job: 'test-job-name1', parameters: [string(name: 'PARAM_NAME1', value: 'some value'),
            											  booleanParam(name: 'bool_PARAM_NAME', value: true)]
                      withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install psutil'
                    sh 'python diskinfo.py &'
                }      
            }, parallelTask2: {
            	build job: 'test-job-name2', parameters: [string(name: 'PARAM_NAME1', value: 'some value'),
            											  booleanParam(name: 'bool_PARAM_NAME', value: true)]
                      echo'hello test1'
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
