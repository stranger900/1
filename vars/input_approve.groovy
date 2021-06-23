def input_approve(){     
     input(
                 message: 'Should we continue?', 
                 parameters: 
                 [name: 'Approval', defaultValue: 'YES', description: 'Are you sure to continue ?']
          )       
}
