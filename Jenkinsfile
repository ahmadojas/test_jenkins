pipeline {
    agent any

    parameters {
        string name: "INSTANCE_ID",
            description: "The instance ID of the data engine",
            trim: true

        string name: "AWS_ACCOUNT_ID",
            description: "The account ID that the instance lives in",
            trim: true

        string name: "AWS_REGION",
            description: "The region the instance lives in",
            trim: true

        choice name: "ACTION",
            description: "Whether to enable or disable the sl1_support account",
            choices: ["activate", "suspend"]

        choice name: "DURATION",
            description: "How long to leave the sl1_admin account enabled",
            choices: ["1","2","4","8","16"]
    }

	
		stages {
			stage("Validate inputs") {
            agent any
            steps {
                script {
                    if ( params.INSTANCE_ID != /(^i-[a-f0-9])+$/) {
                        error("Invalid INSTANCE_ID")
                    }

                    if (! params.AWS_ACCOUNT_ID =~ /^\d+$/) {
                        error("Invalid AWS_ACCOUNT_ID")
                    }

                    if (! params.AWS_REGION =~ /^\w{2,}-\w+-\d+$/) {
                        error("Invalid AWS_REGION")
                    }

                    if (! params.ACTION in ["activate", "suspend"]) {
                        error("Invalid ACTION selected")
                    }

                    if (! params.DURATION =~ /\d+/) {
                        error("Invalid DURATION selected")
                    }
                }
            }
        }
		
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
