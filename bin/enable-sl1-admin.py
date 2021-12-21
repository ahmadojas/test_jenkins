import requests
import pymysql
import jenkins
from requests.auth import HTTPBasicAuth
import re
import requests
import time

job_name = "test_jenkins"   #Give your job name here



matches = ["Cannot determine whether to activate or suspend sl1_admin", "Unable to obtain credentials for", "Unable to send command to",
           "sl1_support user has been enabled", "sl1_suppoert has NOT been enabled"]
##all_matches = [item for item in console_output if any(chars in item for chars in matches)]
##
##print("\n".join([i for i in all_matches]))



def enable_sl1_support(job_name, INSTANCE_ID, ACCOUNT_ID, AWS_REGION, ACTION):
    """
    This function enables sl1_support account on customer portal by triggering the jenkins job. and returns the output log.
    """

    server = jenkins.Jenkins('http://localhost:8080', username='ahmad', password='randompassword')
    server.build_job(job_name, {'INSTANCE_ID': INSTANCE_ID, 'ACCOUNT_ID': ACCOUNT_ID, 'AWS_REGION': AWS_REGION, 'ACTION': ACTION})

    try:
        url  = "http://localhost:8080/job/%s/lastBuild/api/json" %job_name   #Replace 'your_jenkins_endpoint' with your Jenkins URL
        while True:
            data = requests.get(url, auth = HTTPBasicAuth('ahmad', 'randompassword')).json()
            if data['building']:
                print("Job is building")
                time.sleep(5)
            else:
                if data['result'] == "SUCCESS":
                        return True
                else:
                        return False
    except Exception as e:
        print(str(e))
        return False


if __name__ == "__main__":
        if enable_sl1_support(job_name, "INSTANCE_ID", "ACCOUNT_ID", "AWS_REGION", "activate"):
                print("Job is success")
        else:
                print("Job status failed")






###!/usr/bin/env python
##import os
##import json
##import boto3
##import time
##
##parameter1 = os.environ['parameter1']
##parameter2 = os.environ['parameter2']
##
##def main():
##    # Parameters :: instanceid,region_name
##    instanceid = "i-063de1af7ebc39fb7"
##    time.sleep(5)
##    print("This is ", parameter1)
##    time.sleep(5)
##    print("Wishing you ", parameter2)
##    time.sleep(5)
####    ssm_client = boto3.client("ssm", region_name="ap-south-1",)
####    responce = ssm_client.send_command(InstanceIds=[
####                                       instanceid], DocumentName="AWS-RunShellScript",
####                                       Parameters={"commands": ["hostname"]})
####    command_id = responce["Command"]["CommandId"]
####    output = ssm.client.get_command_invocation(
####        CommandId=command_id,
####        InstanceId=instanceid
####    )
####    while output["Status"] == "InProgress":
####        output = ssm.client.get_command_invocation(
####            CommandId=command_id,
####            InstanceId=instanceid
####        )
####    return output["StandardOutputContent"]
##
##
##if __name__ == "__main__":
##    main()
