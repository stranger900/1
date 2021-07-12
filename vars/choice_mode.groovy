def call(){
                  if (env.BUILD_NUMBER.toInteger() % 2 == 0){
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
