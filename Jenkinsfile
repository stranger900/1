@Library("shared-libraries-input") _
pipeline{
    agent {label 'ubuntu'}
    
    environment{
        IMAGE_NAME = "webapp" 
        LOGIN = "andriy900"
        DC_PORT_NUMBER = "80"
        BRANCH_NAME = "${GIT_BRANCH.toLowerCase().replaceAll('^[0-9]', '').replaceAll('[^a-z0-9]', '-').replaceAll('-+', '-').replaceAll('(^-+|-+$)', '').take(63)}"
        ENV = "${BRANCH_NAME == 'master' ? 'prod' : 'dev'}"
        DOCKERHUB_CRED = credentials('dockerhub')
        IP_ADDRESS = "192.168.1.15"
    }    
    options {
        properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '5')), pipelineTriggers([[$class: 'ComputedFolderWebHookTrigger', token: 'mytoken']])])    }
    stages{
//         stage('Approve') {
//             steps {
//                 input_port()
                 
//             }    
//         } 
        stage("Docker Build"){
          steps {
                docker_build_push()
          }    
        }
        stage('Install modules') {
          steps {
               sh 'export ANSIBLE_COLLECTIONS_PATHS="$WORKSPACE/collections"'
             sh 'ansible-galaxy collection install community.docker -p $WORKSPACE/collections'
          }
        }
        stage('Choice mode') {
          steps {
              choice_mode()              
          }
        }
        stage('Deploy app') {
          steps {              
                  ansiblePlaybook credentialsId: 'private-key', vaultCredentialsId: 'ansible_vault', extraVars:[env: "${ENV}", branch_name: "${BRANCH_NAME}", build_number: "${BUILD_NUMBER}", docker_cred: "${DOCKERHUB_CRED_USR}", image_name: "${IMAGE_NAME}", dc_port_number: "${DC_PORT_NUMBER}", port_number: "${PORT_NUMBER}", mode: "${MODE}", db_linc: "${DB_LINC}" ], installation: 'ansible', inventory: 'hosts', playbook: 'main.yml'    
          }          
        }
        stage('downstream job'){
            steps {
            build job: 'test_app', parameters: [string(name: 'IP_ADDRESS', value: "${IP_ADDRESS}"), string(name: 'PORT_NUMBER', value: "${PORT_NUMBER}")]
            
            }
        }    
    }
}
