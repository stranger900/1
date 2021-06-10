pipeline{
    agent any
    
    environment{
        IMAGE_NAME = "webapp" 
        // BRANCH_NAME = "${GIT_BRANCH.toLowerCase().replaceAll('^[0-9]', '').replaceAll('[^a-z0-9]', '-').replaceAll('-+', '-').replaceAll('(^-+|-+$)', '').take(63)}"
        BRANCH_NAME = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
        ENV = "${$BRANCH_NAME == 'master' ? 'dev' : 'prod'}"
        DOCKERHUB_CRED = credentials('dockerhub')   
    }    
    stages{
        stage('Git init'){
            steps{
                git 'https://github.com/stranger900/1.git'
            }
        }
        // stage('Docker Build and Tag') {
        //   steps {
              
        //       sh 'docker build -t ${DOCKERHUB_CRED_USR}/${IMAGE_NAME}${GIT_BRANCH}:${BUILD_NUMBER} .'                
               
        //   }
        // }
        stage('Login Docker Hub') {
          steps {
              //sh 'docker login -u lgn -p psw'
              sh 'echo ${DOCKERHUB_CRED_PSW} | docker login -u ${DOCKERHUB_CRED_USR} --password-stdin'
          }
        }
        // stage('Publish image to Docker Hub') {
        //   steps {
        //       sh 'docker push ${IMAGE_NAME}'
        //   }
        // }
        stage ('Checkout') {
          steps {
            
            echo "$BRANCH_NAME"
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
              ansiblePlaybook credentialsId: 'private-key', extraVars:[env: "${ENV}"], installation: 'ansible', inventory: 'hosts', playbook: 'play.yml'
              //echo "${GIT_BRANCH}"
          }
        }
        stage('Install docker') {
          steps {
              ansiblePlaybook credentialsId: 'private-key', extraVars:[env: "${ENV}"], installation: 'ansible', inventory: 'hosts', playbook: 'playbook5.yml'
          }
        }
        stage('Deploy') {
          steps {
              ansiblePlaybook credentialsId: 'private-key', extraVars:[env: "${ENV}"], installation: 'ansible', inventory: 'hosts', playbook: 'playbook7.yml'
          }
        }
    }
}
