pipeline{
    agent any
    
    environment{
        IMAGE_NAME = "webapp" 
        LOGIN = "andriy900"
        PORT_NAMBER = "5000"
        BRANCH_NAME = "${GIT_BRANCH.toLowerCase().replaceAll('^[0-9]', '').replaceAll('[^a-z0-9]', '-').replaceAll('-+', '-').replaceAll('(^-+|-+$)', '').take(63)}"
//         BRANCH_NAME = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
        ENV = "${$BRANCH_NAME == 'master' ? 'prod' : 'dev'}"
        DOCKERHUB_CRED = credentials('dockerhub')   
    }    
    stages{
        stage('Docker Build and Tag') {
          steps {
//               sh 'echo $LOGIN > settings.env'
//               sh 'echo $IMAGE_NAME >> settings.env'
//               sh 'echo $BRANCH_NAME >> settings.env'
//               sh 'echo $BUILD_NUMBER >> settings.env'              
              sh 'docker build -t ${DOCKERHUB_CRED_USR}/${IMAGE_NAME}:${BRANCH_NAME}-${BUILD_NUMBER} .'            
          }
        }
        stage('Publish image to Docker Hub') {
          steps {
              withDockerRegistry(credentialsId: 'dockerhub', url: '') {
                  sh 'docker push ${DOCKERHUB_CRED_USR}/${IMAGE_NAME}:${BRANCH_NAME}-${BUILD_NUMBER}'
              }              
          }
        }
        stage('Install modules') {
          steps {
               sh 'export ANSIBLE_COLLECTIONS_PATHS="$WORKSPACE/collections"'
             sh 'ansible-galaxy collection install community.docker -p $WORKSPACE/collections'
          }
        }

        stage('Deploy app') {
          steps {
              ansiblePlaybook credentialsId: 'private-key', vaultCredentialsId: 'ansible_vault', extraVars:[env: "${ENV}", branch_name: "${BRANCH_NAME}", build_number: "${BUILD_NUMBER}", docker_cred: "${DOCKERHUB_CRED_USR}", image_name: "${IMAGE_NAME}", port_number: "${PORT_NAMBER}" ], installation: 'ansible', inventory: 'hosts', playbook: 'main.yml'
          }
        }
    }
}
