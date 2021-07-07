def call(){     
     input_port = input(id: 'userInput', message: 'some message', parameters: [
    [$class: 'ChoiceParameterDefinition', choices: string, description: 'description', name:'input'],
    ])
}
