#!/usr/bin/env python
import os
import json
import boto3
import time

parameter1 = os.environ['parameter1']
parameter2 = os.environ['parameter2']

def main():
    # Parameters :: instanceid,region_name
    instanceid = "i-063de1af7ebc39fb7"
    time.sleep(60)
    print("This is ", parameter1)
    print("Wishing you ", parameter2)
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
