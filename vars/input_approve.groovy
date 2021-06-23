def call(){     
     input(
                 id: 'userInput',
                 message: 'Should we continue?', 
                 ok: 'Approve',
                 parameters: [       string(defaultValue: 'Click "Aprove" to PROCEED',
                                            description: 'Do you want to approve',
                                            name: 'Approval'), 
                             ])       
}
