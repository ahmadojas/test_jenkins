#!/usr/bin/env python
import os
import json
import boto3
import time

INSTANCE_ID = os.environ['INSTANCE_ID']
ACCOUNT_ID = os.environ['AWS_ACCOUNT_ID']
AWS_REGION = os.environ['AWS_REGION']
ACTION = os.environ['ACTION']
DURATION = os.environ['DURATION']
Name = os.getenv
Name1 = os.environ['BUILD_TRIGGER_BY']

def main():
    # Parameters :: instanceid,region_name
    instanceid = "i-063de1af7ebc39fb7"
##    time.sleep(5)
    print("This is ", INSTANCE_ID)
##    time.sleep(5)
    print("Wishing you ", ACCOUNT_ID)
    print("Wishing you a very ", Name)
    print("Wishing you a very beutiful ", Name1)
    with open("test_file.txt", "w+") as f:
        f.write("Hey Triggered Man {}".format(Name1))
        print("File created")
    print(INSTANCE_ID, ACCOUNT_ID, AWS_REGION, ACTION, DURATION)
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
