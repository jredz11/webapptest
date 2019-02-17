
pipeline {
    agent {
        docker {
            image 'maven:3-alpine' 
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
                python './jenkins/scripts/EDAS.py $JENKINS_HOME/workspace/webapptest/target/webapptest.war'
            }
        }
    }
}
