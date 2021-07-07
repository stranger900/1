def call(){     
     env.PORT_NUMBER = input(
        id: 'userInput', message: 'Let\'s promote?', parameters: [
        [$class: 'TextParameterDefinition', defaultValue: 'Enter port number for docker container ( 5010 - 6000 )', description: 'Port number', name: 'pn']
        ])
     echo ("Env: "+env.PORT_NUMBER)
}
