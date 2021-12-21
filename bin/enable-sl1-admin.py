#!/usr/bin/env python
import os
import json
import boto3
import time

INSTANCE_ID = os.environ['INSTANCE_ID']
ACCOUNT_ID = os.environ['ACCOUNT_ID']
AWS_REGION = os.environ['AWS_REGION']
ACTION = os.environ['ACTION']

def main():
    # Parameters :: instanceid,region_name
    instanceid = "i-063de1af7ebc39fb7"
##    time.sleep(5)
    print("This is ", INSTANCE_ID)
##    time.sleep(5)
    print("Wishing you ", ACCOUNT_ID)
##    time.sleep(5)
##    ssm_client = boto3.client("ssm", region_name="ap-south-1",)
##    responce = ssm_client.send_command(InstanceIds=[
##                                       instanceid], DocumentName="AWS-RunShellScript",
##                                       Parameters={"commands": ["hostname"]})
##    command_id = responce["Command"]["CommandId"]
##    output = ssm.client.get_command_invocation(
##        CommandId=command_id,
##        InstanceId=instanceid
##    )
##    while output["Status"] == "InProgress":
##        output = ssm.client.get_command_invocation(
##            CommandId=command_id,
##            InstanceId=instanceid
##        )
##    return output["StandardOutputContent"]


if __name__ == "__main__":
    main()
