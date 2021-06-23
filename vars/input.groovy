def input_approve(){
     input {
                message "Should we continue?"
                ok "Yes, we should."                
                parameters {
                    string(name: 'Approval', defaultValue: 'YES', description: 'Are you sure to continue ?')
                }
            }
}
