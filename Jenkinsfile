pipeline{
    agent any
    
    environment{
        
        DOCKERHUB_CRED = credentials('dockerhub')        
        IMAGE_NAME     = 'andriy900/webapp:${GIT_BRANCH}-${BUILD_NUMBER}' 
        ENV="${GIT_BRANCH.equalsIgnoreCase('master') ? 'PROD' : 'DEV'}"
        
    stages{
        stage('Git init'){
            steps{
                git $GIT_REPO
            }
        }
        stage('Docker Build and Tag') {
          steps {
              
              sh 'docker build -t ${IMAGE_NAME} .'                
               
          }
        }
        stage('Login Docker Hub') {
          steps {
              
              sh 'echo $DOCKERHUB_CRED_PSW | docker login -u $DOCKERHUB_CRED_USR --password-stdin'
          }
        }
        stage('Publish image to Docker Hub') {
          steps {
              sh 'docker push ${IMAGE_NAME}'
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
              ansiblePlaybook credentialsId: 'private-key', installation: 'ansible',  extras: '$ENV', inventory: 'hosts', playbook: 'playbook7.yml'
          }
        }
    }
}
