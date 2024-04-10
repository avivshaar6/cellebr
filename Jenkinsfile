pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Define steps for main branch
                if (env.BRANCH_NAME == 'main') {
                    println("Prod deployment from $env.BRANCH_NAME branch!!!!")
                } else {
                    println("Dev deployment from $env.BRANCH_NAME branch!!!!")
                }
                // Add your build steps here
            }
        }
    }
}