pipeline {
    agent any

    parameters {
        string name: "parameter1",
            description: "The instance ID of the data engine"

        string name: "parameter2",
            description: "The account ID that the instance lives in"
    }

    stages {
        stage("Enable SL1 Admin") {

            steps {
                bat 'echo %path%'
				sh '''#!/usr/bin/env python
				print("Hi Hello Vanakkam")'''
            }
        }
    }
}
