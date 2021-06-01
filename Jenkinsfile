pipeline{
    agent any
    stages{
        stage('Git init'){
            steps{
                git 'https://github.com/stranger900/1.git'
            }
        }
        stage('Execute ansible'){
            steps{
                ansiblePlaybook credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'ansible', inventory: 'hosts', playbook: 'play.yml'
            }
        }
    }
}