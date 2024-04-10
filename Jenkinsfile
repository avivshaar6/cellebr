pipeline {
    agent any
    stages {
        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                // Define steps for main branch
                echo 'Building main branch...'
                // Add your build steps here
            }
        }
        stage('Develop Build') {
            when {
                branch 'develop'
            }
            steps {
                // Define steps for develop branch
                echo 'Building develop branch...'
                // Add your build steps here
            }
        }
    }
}

// node('master'){
//     sh ("docker build -t server:latest --build-arg APP_PORT=4000 .")
//     sh ("docker docker tag server:latest aviv012/server:latest")
//     sh ("push aviv012/server:latest")
// }