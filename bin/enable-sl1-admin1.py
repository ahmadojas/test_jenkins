#!/usr/bin/env python

import os
import sys
import boto3
from csv import DictReader, DictWriter, QUOTE_NONNUMERIC
from datetime import datetime, timedelta
from time import sleep

# SILO_MYSQL_COMMAND = '''sudo silo_mysql -e "update master_access.accounts set state={level} where user = 'sl1_support';"'''
# SILO_MYSQL_COMMAND = "ls -a"
##JENKINS_REMOTE_ROLE = os.getenv("JENKINS_REMOTE_ROLE")
##JOB_NAME = os.getenv("JOB_NAME")
FAILURE = ["Cancelled", "TimedOut", "Failed", "Cancelling"]
COLUMNS = ["timestamp", "action", "account", "instance", "region", "expiry"]

last_thirty_mins_obj = datetime.now() - timedelta(minutes = 80)
last_thirty_mins_timestamp = int(datetime.timestamp(last_thirty_mins_obj))

def main(instance, account, region, action, duration):
    start = datetime.now()
    # epoch = start.strftime("%S")
    epoch = int(datetime.timestamp(start))
    # logpath = f"/usr/local/agent-storage/{JOB_NAME}/{account}.csv"
    
    basepath = f"C:\ProgramData\Jenkins\.jenkins\workspace\\test_jenkins"
    if not os.path.exists(basepath):
        os.mkdir(basepath)
        logpath = os.path.join(basepath, "{account}.csv")
        
    logpath = f"C:\ProgramData\Jenkins\.jenkins\workspace\\test_jenkins\\{account}.csv"
    
    if action == "activate":
        level = 1
    elif action == "suspend":
        level = 0
    else:
        print("Cannot determine whether to activate or suspend sl1_admin")
        exit(1)

    expiry = "NA"
    
    if level == 1:
        expiry = start + timedelta(minutes=int(1))


    # always start with the latest entry at the beginning of the array
    # so that the latest log is at the top of the file
    #
    # subsequent entries are appended later in the array
    logs = [{
        "timestamp": epoch,
        "action": action,
        "account": account,
        "instance": instance,
        "region": region,
        "expiry": int(datetime.timestamp(expiry)) if level == 1 else int(datetime.timestamp(datetime.now()))
    }]

    # if the file exists, open it and read it into the logs array
    # otherwise, create it with 'w'
    if os.path.isfile(logpath):
        logfile = open(logpath, "r")
        reader = DictReader(logfile)
        for log in reader:
            logs.append(log)
    else:
        logfile = open(logpath, "w")

    logfile.close()

##    role_arn = JENKINS_REMOTE_ROLE.format(account)
##    session_name = f"jenkins-{action}-sl1_support-{epoch}"
##
##    # assume the jenkins-agent role in the remote account
##    try:
##        sts = boto3.client("sts")
##        role = sts.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
##    except Exception as e:
##        print(f"Unable to obtain credentials for '{role_arn}'")
##        print(e)
##        exit(1)

##    # start a boto3 session using the credentials we just obtained
##    session = boto3.Session(
##        aws_access_key_id=role["Credentials"]["AccessKeyId"],
##        aws_secret_access_key=role["Credentials"]["SecretAccessKey"],
##        aws_session_token=role["Credentials"]["SessionToken"]
##    )
##
##    # use our session to generate the ssm client in the remote account
##    # and then send the command
##    try:
##        ssm = session.client("ssm", region_name=region)
##        response = ssm.send_command(
##            InstanceIds=[instance],
##            DocumentName="AWS-RunShellScript",
##            Parameters={"commands": [SILO_MYSQL_COMMAND.format(level=level)]}
##        )
##    except Exception as e:
##        print(f"Unable to send command to {instance}")
##        print(e)
##        exit(1)
##
##    command_id = response["Command"]["CommandId"]
##    command_status = response["Command"]["Status"]
##
##    # wait for the command to come into a finished state
##    attempts = 0
##    while attempts < 20:
##        print("entered into while loop")
##        if command_status in FAILURE:
##            print("sl1_suppoert has NOT been enabled")
##            exit(1)
##        elif command_status == "Success":
##            print("sl1_support user has been enabled")
##            break
##        else:
##            sleep(5)
##            attempts += 1
##            
##            try:
##                output = ssm.get_command_invocation(
##                    CommandId=command_id,
##                    InstanceId=instance
##                )
##
##                command_status = output["Status"]
##                print("command_status in while loop", command_status)
##            except Exception:
##                command_status = "Failed"

    print("After while loop")
    logfile = open(logpath, 'w', newline="")
    writer = DictWriter(logfile, fieldnames=COLUMNS, quoting=QUOTE_NONNUMERIC)
    writer.writeheader()
    writer.writerows(logs)
    logfile.close()

    logfile_read = open(logpath, 'r')
    log_reader = DictReader(logfile_read)
    print("log_reader", list(log_reader))
    
    return "Command not complete"

    
def suspend_with_cron():
    
    logpath = f"C:\ProgramData\Jenkins\.jenkins\workspace\\test_jenkins"
    print("Entered into suspend_with_cron function", logpath)
    if os.path.isdir(logpath):
        files = os.listdir(logpath)
        print("Files", files)
        logs = []
        activate_logs = []
        final_activate_logs = []
        suspended_logs = []
        suspended = []
        activated = []
        expired = []
        for file in files:
            if ".csv" in file:
                filepath = os.path.join(logpath, file)
                if os.path.isfile(filepath):
                    logfile = open(logpath+"\\012345678911.csv", "r")
                    reader = DictReader(logfile)
                    list_dicts = reversed(list(reader))
                    print("list_dicts", list_dicts)
##                    for i in list_dicts:
##                        if "activate" in i["action"] and int(i["expiry"]) < int(datetime.timestamp(datetime.now())):
##                            print("iiiiiiiiii", [dict(i)])
##                    activated = [dict(i) if "activate" in i["action"] and int(i["expiry"]) < int(datetime.timestamp(datetime.now())) \
##                                 else suspended.append(dict(i)) for i in list_dicts]

                    for i in list_dicts:
                        print("Kiiiiiiiiiiiiiiii", i['instance'], int(i["expiry"]), int(datetime.timestamp(datetime.now())))
                        if "activate" in i["action"] and int(i["expiry"]) < int(datetime.timestamp(datetime.now())):
                            activated.append(dict(i))
                        elif "suspend" in i["action"]:
                            suspended.append(dict(i))
##                    activated = [dict(i) if "activate" in i["action"] and int(i["expiry"]) < int(datetime.timestamp(datetime.now())) \
##                                 else suspended.append(dict(i)) for i in list_dicts]
                    
                    #suspended = [dict(i) for i in list_dicts if "suspend" in i["action"] and int(i["expiry"]) < int(datetime.timestamp(datetime.now()))]
                    print("activated...", activated)
                    print("suspended...", suspended)
##                    final_activate_logs1 = [activate for activate in activated if (int(activate['expiry']) >= int(log["expiry"])) \
##                                                       and activate['account'] == suspend["account"] and activate['instance'] != log["instance"]]

                    #print(activated, suspended)
##                    final_activate_logs1 = [activate for activate in activated for suspend in suspended if activate and activate['instance'] in suspend and activate['instance'] == suspend["instance"] \
##                                                       and int(activate['expiry']) > last_thirty_mins_timestamp and (int(activate['expiry']) >= int(suspend["expiry"]))]

                    print("last_thirty_mins_timestamp", last_thirty_mins_timestamp)

                    final_activate_logs1 = [activate for activate in activated if activate and int(activate['expiry']) > last_thirty_mins_timestamp ]
                    final_suspended_logs1 = [suspend for suspend in suspended if suspend and int(suspend['expiry']) > last_thirty_mins_timestamp ]

                    if final_suspended_logs1:
                        for last_suspended in final_suspended_logs1:
                            for last_activated in final_activate_logs1:
                                print("Heeeeeeeeee", last_suspended['instance'], last_activated['instance'], int(last_suspended["expiry"]), int(last_activated["expiry"]), "current", int(datetime.timestamp(datetime.now())))
                                if last_suspended['instance'] == last_activated['instance'] and int(last_suspended["expiry"]) < int(datetime.timestamp(datetime.now())) \
                                   and int(last_activated["expiry"]) >= int(last_suspended["expiry"]):
                                    print("\n Suspended matched@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", last_suspended['instance'], last_suspended["expiry"])
                                elif last_suspended['instance'] != last_activated['instance'] and int(last_suspended["expiry"]) < int(datetime.timestamp(datetime.now())):
                                    current = int(datetime.timestamp(datetime.now()))
                                    print("\n Unique1 activated instance availabe", last_activated['instance'], int(last_activated["expiry"]), current)
                                    expired1 = [expire for expire in final_activate_logs1 if int(expire["expiry"]) < int(datetime.timestamp(datetime.now()))]
                                    print("\n Only Unique1 Expired instances available", expired1)
                                    suspended = [suspended for suspended in final_suspended_logs1 if int(suspended["expiry"]) < int(datetime.timestamp(datetime.now()))]
                                    print("\n Only Unique1 suspended instances available", suspended)

                                    instance_ids = [d['instance'] for d in expired1]
                                    print("\n instance_ids", instance_ids)
                                    activated_instance_ids = []
                                    suspended_instance_ids = [x for x in suspended if x['instance'] in instance_ids and x!=None ]
                                    print("\n suspended_instance_ids", suspended_instance_ids)

                                    if suspended_instance_ids:
                                        for susp_ins_ids in suspended_instance_ids:
                                            for d in expired1:
                                                if susp_ins_ids and d and susp_ins_ids['instance'] == d['instance'] and int(susp_ins_ids['expiry']) <= int(d['expiry']):
                                                    print("pooooooooooooooooooooooooooo", susp_ins_ids)
                                                    continue
                                                elif susp_ins_ids and d and susp_ins_ids['instance'] == d['instance'] and int(susp_ins_ids['expiry']) <= int(d['expiry']):
                                                    print("Expireddddd", d)
                                    elif expired1:
                                        expired = expired1
                                    #activated_instance_ids = [x for x in expired1 if x['instance'] not in instance_ids]
##                                    print("\n activated_instance_ids", activated_instance_ids)
##                                    print("\n kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", expired1)
##                                    if suspended_instance_ids:
##                                        expired = [x for x in suspended if x['instance'] not in suspended_instance_ids]
##                                    else:
##                                        expired = expired1
                                    print("\n Hohooooooooooooooo", expired)
                                    not_expired = [expire for expire in final_activate_logs1 if int(expire["expiry"]) > int(datetime.timestamp(datetime.now()))]
                                    print("\n Not Expired Unique1 instances available", not_expired)
                                    continue
                                else:
                                    print("\n Unique activated instance without prev history matched@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                                    expired1 = [expire for expire in final_activate_logs1 if int(expire["expiry"]) < int(datetime.timestamp(datetime.now()))]
                                    print("\n Only Unique Expired instances available", expired1)

                                    suspended = [suspended for suspended in final_suspended_logs1 if int(suspended["expiry"]) < int(datetime.timestamp(datetime.now()))]
                                    print("\n Only Unique suspended instances available", suspended)

                                    instance_ids = [d['instance'] for d in expired1]
                                    print("\n instance_ids", instance_ids)
                                    activated_instance_ids = []
                                    suspended_instance_ids = [x for x in suspended if x['instance'] in instance_ids and x!=None ]
                                    print("\n suspended_instance_ids", suspended_instance_ids)

                                    if suspended_instance_ids:
                                        for susp_ins_ids in suspended_instance_ids:
                                            for d in expired1:
                                                print("lllllooooooo", d, susp_ins_ids['instance'] == d['instance'], int(susp_ins_ids['expiry']), int(d['expiry']), int(susp_ins_ids['expiry']) <= int(d['expiry']))
                                                if susp_ins_ids and d and susp_ins_ids['instance'] == d['instance'] and int(susp_ins_ids['expiry']) <= int(d['expiry']):
                                                    print(d, "pooooooooooooooooooooooooooo", susp_ins_ids)
                                                    expired = [d]
                                                    #continue
                                                elif susp_ins_ids and d and susp_ins_ids['instance'] == d['instance'] and int(susp_ins_ids['expiry']) <= int(d['expiry']):
                                                    print("Expireddddd", d)
                                                else:
                                                    print("woooooooooooo", d)
                                                #print(susp_ins_ids['instance'] == d['instance'], int(susp_ins_ids['expiry']), int(d['expiry']), int(susp_ins_ids['expiry']) <= int(d['expiry']))
                                    elif expired1:
                                        expired = expired1
                                    #activated_instance_ids = [x for x in expired1 if x['instance'] not in instance_ids]
##                                    print("\n activated_instance_ids", activated_instance_ids)
##                                    print("\n kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", expired1)
##                                    if suspended_instance_ids:
##                                        expired = [x for x in suspended if x['instance'] not in suspended_instance_ids]
##                                    else:
##                                        expired = expired1
                                    print("\n Hohooooooooooooooo11111", expired)
                                    
                                    not_expired = [expire for expire in final_activate_logs1 if int(expire["expiry"]) > int(datetime.timestamp(datetime.now()))]
                                    print("\n Not Expired Unique instances available", not_expired)
                    elif final_activate_logs1:
                        print("\n Only activated instances available", final_activate_logs1)
                        expired = [expire for expire in final_activate_logs1 if int(expire["expiry"]) < int(datetime.timestamp(datetime.now()))]
                        print("\n Only Expired instances available", expired)
                        not_expired = [expire for expire in final_activate_logs1 if int(expire["expiry"]) > int(datetime.timestamp(datetime.now()))]
                        print("\n Not Expired instances available", not_expired)
                    else:
                        print("\n Neither activated or suspended instances available", final_activate_logs1)

                    print("Activated  Aaaaaaavoooooooo", final_activate_logs1)
                    print("Suspended  Aaaaaaavoooooooo", final_suspended_logs1)
##                    for log in list_dicts:
##                        logs.append(dict(log))
####                        if log["action"] == "activate" and int(log["expiry"]) < int(datetime.timestamp(datetime.now())):
####                            activate_logs.append(dict(log))
####                            #print("if ativate cond", dict(log))
##                        if log["action"] == "suspend":
##                            suspended_logs.append(dict(log))
##                            if activated and [log["instance"] in activate["instance"] for activate in activated] \
##                               and [int(log["expiry"]) >= int(activate["expiry"]) and activate['instance'] == log["instance"] for activate in activated]:
##                                #print(activate_logs.index(list(log.values())))
##                                print("activated-------------------------------------------------------------------------", activated)
##                                print("suspended-------------------------------------------------------------------------", dict(log))
##                                final_activate_logs = [activate for activate in activated if (int(activate['expiry']) >= int(log["expiry"])) \
##                                                       and activate['account'] == suspend["account"] and activate['instance'] != log["instance"]]
##                                print("\n after suspended................................................", final_activate_logs)
##                                #activate_logs.append(log.values())
##                        print("first", log["action"] == "suspend", activated, log["action"] == "suspend" and [log["instance"] in item["instance"] for item in activated])
##                        print("second", log["action"] == "suspend" and [log["instance"] in item["instance"] for item in activated] and [int(log["expiry"]) >= int(item["expiry"]) for item in activated])
##                        
                    logfile.close()
                
    ##            logfile = open(filepath, 'w')
    ##            writer = DictWriter(logfile, fieldnames=COLUMNS, quoting=QUOTE_NONNUMERIC)
    ##            writer.writeheader()
    ##            writer.writerows(activate_logs)
    ##            logfile.close()

##        print("logs after append", logs)
        print("\n activate_logs after append", activate_logs)
        print("\n final_activate_logs after append", final_activate_logs)

##        if not final_activate_logs and activate_logs:
##            final_activate_logs = activate_logs

        if expired:
            print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii", expired, type(expired))
            for log in expired:
                # print("for loop log", log)
                if log["action"] == "activate" and int(log["expiry"]) < int(datetime.timestamp(datetime.now())):
                    #pass
                    print("\n Expired instances details : ", log)
                    #main(log["instance"], log["account"], log["region"], "suspend", log["expiry"])
                else:
                    print("There are no expired instaces")
##        elif activate_logs:
##            print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
##            for log in activate_logs:
##                #print("for loop log", log)
##                if log["action"] == "activate" and int(log["expiry"]) < int(datetime.timestamp(datetime.now())):
##                    #pass
##                    print("\n Expired instances details : ", log)
##                    #main(log["instance"], log["account"], log["region"], "suspend", log["expiry"])
##                else:
##                    print("There are no expired instaces")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        instance = sys.argv[1]
        account = sys.argv[2]
        region = sys.argv[3]
        action = sys.argv[4]
        duration = sys.argv[5]
        main(instance, account, region, action, duration)
    else:
        suspend_with_cron()
