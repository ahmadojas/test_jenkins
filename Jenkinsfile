pipeline {
    agent { label 'python3' }

    parameters {
        string name: "INSTANCE_ID",
            description: "The instance ID of the data engine"

        string name: "ACCOUNT_ID",
            description: "The account ID that the instance lives in"

        string name: "AWS_REGION",
            description: "The region the instance lives in"
    }

    stages {
        stage("Enable SL1 Admin") {
            steps {
                sh "${env.WORKSPACE}/bin/enable-sl1-admin.py '${params.INSTANCE_ID}' '${params.ACCOUNT_ID}' '${params.AWS_REGION}'"
            }
        }
    }
}
