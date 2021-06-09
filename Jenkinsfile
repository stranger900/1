pipeline{
    agent any
    environment{
        DOCKERHUB_CRED = credentials('dockerhub')
        WORKSPACE = '/var/lib/jenkins/workspace/test'
    }
    stages{
        stage('Git init'){
            steps{
                git 'https://github.com/stranger900/1.git'
            }
        }
        stage('Docker Build and Tag') {
          steps {
              
                sh 'docker build -t andriy900/webapp:latest .'                
               
          }
        }
        stage('Login Docker Hub') {
          steps {
              
              sh 'echo $DOCKERHUB_CRED_PSW | docker login -u $DOCKERHUB_CRED_USR --password-stdin'
          }
        }
        stage('Publish image to Docker Hub') {
          steps {
              sh 'docker push andriy900/webapp:latest'
          }
        }
        
        stage('Install modules') {
          steps {
               sh 'export ANSIBLE_COLLECTIONS_PATHS="$WORKSPACE/collections"'
             sh 'ansible-galaxy collection install community.docker -p $WORKSPACE/collections'
          }
        }
        stage('Ping') {
          steps {
              ansiblePlaybook credentialsId: 'private-key', installation: 'ansible', inventory: 'hosts', playbook: 'play.yml'
          }
        }
        stage('Install docker') {
          steps {
              ansiblePlaybook credentialsId: 'private-key', installation: 'ansible', inventory: 'hosts', playbook: 'playbook5.yml'
          }
        }
        stage('Deploy') {
          steps {
              ansiblePlaybook credentialsId: 'private-key', installation: 'ansible', inventory: 'hosts', playbook: 'playbook7.yml'
          }
        }
    }
}
