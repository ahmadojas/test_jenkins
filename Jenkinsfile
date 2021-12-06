pipeline {
    agent { docker { image 'python:3.5.1' } }

    parameters {
        string name: "parameter1",
            description: "The instance ID of the data engine"

        string name: "parameter2",
            description: "The account ID that the instance lives in"
    }

    stages {
        stage("Enable SL1 Admin") {
            steps {
                sh "${env.WORKSPACE}/bin/enable-sl1-admin.py '${params.parameter1}' '${params.parameter2}'"
            }
        }
    }
}
