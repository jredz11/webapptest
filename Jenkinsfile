
pipeline {
    agent {
        docker {
            image 'openkbs/jre-mvn-py3' 
            args '-v /root/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'mvn -B -DskipTests clean package' 
            }
        }
      stage('Deliver') {
            steps {
                sh './jenkins/scripts/pythoninstall.sh'
            }
        }
    }
}
