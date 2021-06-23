def call(Map config = [:]){
    sh 'docker build -t ${config.DOCKERHUB_CRED_USR}/${config.IMAGE_NAME}:${config.BRANCH_NAME}-${config.BUILD_NUMBER} .'     
}
