pipeline {
    agent { label 'python' }

    parameters {
        string name: "parameter1",
            description: "The instance ID of the data engine"

        string name: "parameter2",
            description: "The account ID that the instance lives in"
    }

    stages {
        stage("Enable SL1 Admin") {

            steps {
                sh '''#!/usr/bin/env python
print("Hi Hello")
'''
            }
        }
    }
}
