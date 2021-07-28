def call(){
                    env.count = sh(returnStdout: true, script: 'git diff --name-only  @~..@ docker | wc -l').trim()
                    if ( env.count.toInteger() > 0){
                        //docker_build(dockerhub_cred:"${DOCKERHUB_CRED_USR}", image_name:"${IMAGE_NAME}", branch_name:"${BRANCH_NAME}", build_number:"${BUILD_NUMBER}")
                        sh 'docker build -t --no-cache ${DOCKERHUB_CRED_USR}/${IMAGE_NAME}:${BRANCH_NAME}-latest docker/'  
                        withDockerRegistry(credentialsId: 'dockerhub', url: '') {
                            sh 'docker push ${DOCKERHUB_CRED_USR}/${IMAGE_NAME}:${BRANCH_NAME}-latest'
                        }    
                        sh( "git diff --name-only  @~..@ docker")
                        echo "${count}"
                        echo "Docker build`ve done"
                    }else{
                        echo "Docker build haven`t done"
                    } 
}
