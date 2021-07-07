def call(){     
     PORT_NUMBER = input(id: 'userInput', message: 'some message', parameters: [
    [$class: 'ChoiceParameterDefinition', choices: string, description: 'description', name:'input'],
    ])
}
