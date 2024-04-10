pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script{
                    if (env.BRANCH_NAME == 'main') {
                        println("Prod deployment from $env.BRANCH_NAME branch!!!!")
                    } else {
                        println("Dev deployment from $env.BRANCH_NAME branch!!!!")
                    }
                }
            }
        }
    }
}