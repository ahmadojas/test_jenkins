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
                PYTHONPATH='C:/Users/ab18145/AppData/Local/Programs/Python/Python37'
            }
            steps {
                bat 'echo %path%'
				bat 'echo "helooo"'
				bat 'python ./bin/enable-sl1-admin.py'
            }
        }
    }
}
