def call(){     
     input_port_number = input(id: 'userInput', message: 'some message', parameters: [
    [$class: 'ChoiceParameterDefinition', choices: string, description: 'description', name:'input'],
    ])
}
