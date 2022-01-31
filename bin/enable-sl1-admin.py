#!/usr/bin/env python
import os
import json
import boto3
import time
import logging
import sys
import requests


access_url = requests.get("https://m6yuvlc9uk.execute-api.us-east-2.amazonaws.com/dev/access-db-from-jenkins")
retrieved_data = access_url.json()
print("retrieved_data", retrieved_data)

print("hsgshg", sys.argv)
enabled_file_name = 'sl1_users_enabled.log'
suspended_file_name = 'sl1_users_suspended.log'

logging.basicConfig(level=logging.DEBUG, filename=enabled_file_name, format='%(asctime)s %(levelname)s: %(message)s')
logger1 = logging.getLogger()
# print("handlers", logger1.handlers)
first = logger1.handlers[0]
print("first handler", first)

def main(instance, account, region, action, duration):
    # Parameters :: instanceid,region_name
    instanceid = "i-063de1af7ebc39fb7"
    print("This is ", INSTANCE_ID)

    print("Wishing you ", ACCOUNT_ID)
    print("Wishing you a very ", Name)
    print("Wishing you a very beutiful ", Name1)
##    with open("test_file.txt", "w+") as f:
##        print("Writing into the file")
##        f.write("Hey Triggered Man {}".format(Name1))
##        # print("File created")
##    with open("test_file.txt", "r") as fr:
##        print("Reading from file")
##        print("Lines wriiten in the file are : \n", fr.read())   
    print(INSTANCE_ID, ACCOUNT_ID, AWS_REGION, ACTION, DURATION)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("dir_path", dir_path)
    cwd = os.getcwd()
    print("cwd", cwd)

    basepath = f"C:\ProgramData\Jenkins\.jenkins\workspace\\test_jenkins"
    if not os.path.exists(basepath):
        print("Hiiiiiiiiiiiiiiiii")
        os.mkdir(basepath)
        logpath = os.path.join(basepath, "{account}.csv")
        
    logpath = f"C:\ProgramData\Jenkins\.jenkins\workspace\\test_jenkins\\{account}.csv"
    
    # logpath = f"/usr/local/agent-storage/{enabled_file_name}/{account}.log"
    print("Test log path", logpath)

    print("Checking path", os.path.isfile(logpath))
    
    try:
        #"hi" + 2
        data = {"instance_id": instance, "aws_account_id": account, "aws_region": region, "action": action, "duration": duration}
        if action == 'activate':
            data1 = ", ".join(data.values())
            print("activate data1", data1)
            logging.info(data1)
        elif action == 'suspend':
            f = open(enabled_file_name, 'r')
            data['action'] = 'activate'
            data1 = ", ".join(data.values())
            print("suspend data1", data1)
            lines = f.readlines()
            print("lines", lines)
            f.close()
            f1 = open(enabled_file_name, 'w+')
            for line in lines:
                if data1 not in line:
                    print("line", line)
                    f1.write(line)
                    
                else:
                    logger1.removeHandler(first)
                    logging.basicConfig(level=logging.DEBUG, filename=suspended_file_name, format='%(asctime)s %(levelname)s: %(message)s')
                    #logger1.removeHandler(first)
                    print("handlers1111111", logger1.handlers)
                    #logger = logging.getLogger()
                    data['action'] = 'suspend'
                    data2 = ", ".join(data.values())
                    print("Deleting... ", data1)
                    logging.info(data2)
        else:
            print('Please pass valid command as action')
    except Exception as e:
        logger1.exception(e)
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


def test_cond(param1):
    print("test_cond function trigger with suspend params ", param1)


if __name__ == "__main__":
##    instance = sys.argv[1]  # 'i-hgsdh223b' 
##    account =  sys.argv[2]  # '12345678'
##    region =   sys.argv[3]  # 'ap-south-2'
##    action =   sys.argv[4]  # 'suspend'
##    # duration = '2'
##    if len(sys.argv) > 5:
##        duration = sys.argv[5]  # sys.argv[5]
##    else:
##        duration = None
##
##    create_log(instance, account, region, action, duration)
    print(sys.argv)
    if len(sys.argv) > 2:
        instance = sys.argv[1]  # 'i-hgsdh223b' 
        account =  sys.argv[2]  # '12345678'
        region =   sys.argv[3]  # 'ap-south-2'
        action =   sys.argv[4]  # 'suspend'
        # duration = '2'
        if len(sys.argv) > 5:
            duration = sys.argv[5]  # sys.argv[5]
        else:
            duration = None
##        INSTANCE_ID = os.environ['INSTANCE_ID']
##        ACCOUNT_ID = os.environ['AWS_ACCOUNT_ID']
##        AWS_REGION = os.environ['AWS_REGION']
##        ACTION = os.environ['ACTION']
##        DURATION = os.environ['DURATION']
##        Name = os.getenv
##        Name1 = os.environ['BUILD_TRIGGER_BY']
##        main(INSTANCE_ID, ACCOUNT_ID, AWS_REGION, ACTION, DURATION)
    else:
        test_cond(sys.argv[1])
