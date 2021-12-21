pipeline {
    agent any

    parameters {
        string name: "INSTANCE_ID",
            description: "The instance ID of the data engine",
            trim: true
 
        string name: "ACCOUNT_ID",
            description: "The account ID that the instance lives in",
            trim: true
 
        string name: "AWS_REGION",
            description: "The region the instance lives in",
            trim: true
 
        choice name: "ACTION",
            description: "Whether to enable or disable the sl1_support account",
            choices: ["activate", "suspend"]
    }

    stages {
        stage("Enable SL1 Admin") {
		environment {
                PYTHONPATH='C:/Users/ab18145/AppData/Local/Programs/Python/Python37'
            }
            steps {
				bat 'echo "helooo"'
				bat 'python -u ./bin/enable-sl1-admin.py'
            }
        }
    }
}
