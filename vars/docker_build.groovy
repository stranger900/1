def call(Map config = [:]){
    sh 'docker build -t ${config.dockerhub_cred}/${config.image_name}:${config.branch_name}-${config.build_number} .'     
}
