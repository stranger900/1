def input_approve(){     
     input(
                 id: 'userInput'
                 message: 'Should we continue?', 
                 parameters: [

                                    string(defaultValue: 'None',
                                            description: 'Do you want to approve',
                                            name: 'Approval'),                                                            
         
          ])       
}
