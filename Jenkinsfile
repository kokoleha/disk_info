node {
    agent { docker { image 'python:latest'} }
    parallel firstBranch: {
        // do something
         stage('build') {
            steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install psutil'
                    sh 'python diskinfo.py'
                }      
         }
    }, secondBranch: {
        // do something else
        stage('test') {
            sleep 20
            echo 'do some tests1'
            sleep 20
            echo 'do some tests2'

        }
    },
    failFast: true|false
}
