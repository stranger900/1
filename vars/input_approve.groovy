def input_approve(){     
     input(
                 message: 'Should we continue?', 
                 parameters: [
                 string(name: 'Approval', defaultValue: 'YES', description: 'Are you sure to continue ?')
          ])       
}
