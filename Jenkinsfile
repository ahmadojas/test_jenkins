pipeline {
    agent any

    parameters {
        validatingString(
            name: "INSTANCE_ID",
            defaultValue: "",
            regex: /^([a-zA-Z0-9_-]){19}$/, 
            failedValidationMessage: "Validation failed!", 
            description: "Please provide the Alphanumeric instance id with length ex: i-2d9dab0a24fe2c44c")
        validatingString(
            name: "AWS_ACCOUNT_ID",
            defaultValue: "",
            regex: /^([0-9_-]){12}$/, 
            failedValidationMessage: "Validation failed!", 
            description: "Please provide the Numeric account id with the length 12 ex: 012345678911")
        validatingString(
            name: "AWS_REGION",
            defaultValue: "",
            regex: /^[a-z\d\-_\s]+$/, 
            failedValidationMessage: "Validation failed!", 
            description: "Please provide the Alphanumeric aws region ex: ap-south-1")
        choice name: "ACTION",
            description: "Enable or Disable the sl1_support account",
            choices: ["activate", "suspend"]
        choice name: "Uptime",
            description: "Account would be disabled after the period of selected time note: duration would be in hrs only!",
            choices: ["2 hrs","4 hrs","6 hrs","8 hrs","12 hrs","24 hrs"]
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
