def call(){     
     userInput = input(
        id: 'userInput', message: 'Let\'s promote?', parameters: [
        [$class: 'TextParameterDefinition', defaultValue: 'uat', description: 'Environment', name: 'env']
        ])
     echo ("Env: "+userInput)
}
