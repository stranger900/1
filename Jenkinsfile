@Library("shared-libraries-input") _
pipeline{
    agent {label 'ubuntu'}
    
    environment{
        IMAGE_NAME = "webapp" 
        LOGIN = "andriy900"
        //PORT_NUMBER = "${BUILD_NUMBER.intdiv(2) == 1 ? '5010' : '5012'}"
        DC_PORT_NUMBER = "80"
        BRANCH_NAME = "${GIT_BRANCH.toLowerCase().replaceAll('^[0-9]', '').replaceAll('[^a-z0-9]', '-').replaceAll('-+', '-').replaceAll('(^-+|-+$)', '').take(63)}"
        ENV = "${BRANCH_NAME == 'master' ? 'prod' : 'dev'}"
        DOCKERHUB_CRED = credentials('dockerhub')   
    }    
    stages{
//         stage('Approve') {
//             steps {
//                 input_port()
                 
//             }    
//         } 
//         stage('Docker Build and Tag') {
//           steps {  
//               docker_build(dockerhub_cred:"${DOCKERHUB_CRED_USR}", image_name:"${IMAGE_NAME}", branch_name:"${BRANCH_NAME}", build_number:"${BUILD_NUMBER}")
//               //sh 'docker build -t ${DOCKERHUB_CRED_USR}/${IMAGE_NAME}:${BRANCH_NAME}-${BUILD_NUMBER} .'            
//           }
//         }
//         stage('Publish image to Docker Hub') {
//           steps {
//               withDockerRegistry(credentialsId: 'dockerhub', url: '') {
//                   sh 'docker push ${DOCKERHUB_CRED_USR}/${IMAGE_NAME}:${BRANCH_NAME}-${BUILD_NUMBER}'
//               }              
//           }
//         }
        stage('Install modules') {
          steps {
               sh 'export ANSIBLE_COLLECTIONS_PATHS="$WORKSPACE/collections"'
             sh 'ansible-galaxy collection install community.docker -p $WORKSPACE/collections'
          }
        }
        stage('Choice mode') {
          steps {
              script {
              //ansiblePlaybook credentialsId: 'private-key', vaultCredentialsId: 'ansible_vault', extraVars:[env: "${ENV}", branch_name: "${BRANCH_NAME}", build_number: "${BUILD_NUMBER}", docker_cred: "${DOCKERHUB_CRED_USR}", image_name: "${IMAGE_NAME}", dc_port_number: "${DC_PORT_NUMBER}", port_number: "${PORT_NUMBER}" ], installation: 'ansible', inventory: 'hosts', playbook: 'main.yml'
                  if (BUILD_NUMBER.toInteger() % 2 == 0){
                       env.MODE = "green"
                       env.PORT_NUMBER = 5010
                       env.DB_LINC = "green-server.com"
                       echo "Mode of deployment is ${MODE}"
                       echo "Port number of docker container is ${PORT_NUMBER}"
                  }else{
                       env.MODE = "blue"
                       env.PORT_NUMBER  = 5012
                       env.DB_LINC = "blue-server.com"
                       echo "Mode of deployment is ${MODE}"
                       echo "Port number of docker container is ${PORT_NUMBER}" 
                  }                  
          }
        }
    }
        stage('Deploy app') {
          steps {              
                  ansiblePlaybook credentialsId: 'private-key', vaultCredentialsId: 'ansible_vault', extraVars:[env: "${ENV}", branch_name: "${BRANCH_NAME}", build_number: "${BUILD_NUMBER}", docker_cred: "${DOCKERHUB_CRED_USR}", image_name: "${IMAGE_NAME}", dc_port_number: "${DC_PORT_NUMBER}", port_number: "${PORT_NUMBER}", mode: "${MODE}", db_linc: "${DB_LINC}" ], installation: 'ansible', inventory: 'hosts', playbook: 'main.yml'    
                  echo "Mode of deployment is ${MODE}"
                  echo "Mode of deployment is ${PASSW_BLUE}"
                  echo "Mode of deployment is ${PASSW_GREEN}"          }
          
        }
    }
}
