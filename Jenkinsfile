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
		environment {
                PYTHONPATH='/usr/lib/python3.10:/usr/lib/python3:/usr/var/lib/python3.10:/usr/var/lib/python3'
            }
            steps {
                sh "echo Hello world"
            }
        }
    }
}
