def call(){     
     env.PORT_NUMBER = input(
        id: 'userInput', message: 'Enter port number', parameters: [
        [$class: 'TextParameterDefinition', defaultValue: '', description: 'and press proceed', name: 'Enter port number for docker container ( 5010 - 6000 )']
        ])
     echo ("Env: "+env.PORT_NUMBER)
}
