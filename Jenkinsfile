pipeline {
    agent any

    environment {
        // Jenkins runs as a macOS service with a minimal PATH, so add Docker and Homebrew tools
        PATH = "/Applications/Docker.app/Contents/Resources/bin:/opt/homebrew/bin:/usr/local/bin:${env.PATH}"

        STUDENT_NAME    = 'Dias'
        STUDENT_SURNAME = 'Abdullayev'
        STUDENT_GROUP   = 'IT2-2313SE'
        STUDENT_ID      = '37240'

        IMAGE_NAME     = 'abdullayev-dias-devops'
        CONTAINER_NAME = 'abdullayev-dias-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --pretty="Commit used by Jenkins: %h %s (%an)"'
            }
        }

        stage('Build') {
            steps {
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
                sh 'bash -n scripts/Abdullayev_Dias_system.sh'
                sh 'python3 -m py_compile app/app.py app/test_app.py'
                sh 'chmod +x scripts/Abdullayev_Dias_system.sh'
            }
        }

        stage('Test') {
            steps {
                sh 'test -f Abdullayev_Dias_info.txt && cat Abdullayev_Dias_info.txt'
                sh './scripts/Abdullayev_Dias_system.sh'
                sh 'cd app && python3 -m unittest -v test_app'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest .'
                sh 'docker images ${IMAGE_NAME}'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker rm -f ${CONTAINER_NAME} || true'
                sh '''
                    docker run -d -p 8081:8080 \
                      -e STUDENT_NAME=${STUDENT_NAME} \
                      -e STUDENT_SURNAME=${STUDENT_SURNAME} \
                      -e STUDENT_GROUP=${STUDENT_GROUP} \
                      -e STUDENT_ID=${STUDENT_ID} \
                      --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                '''
                sh 'sleep 3 && docker ps --filter name=${CONTAINER_NAME}'
                sh 'docker logs ${CONTAINER_NAME}'
                sh 'curl -sf http://localhost:8081'
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully!' }
        failure { echo 'Pipeline failed - check the stage marked in red.' }
    }
}
