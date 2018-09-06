#!/usr/bin/python

import boto3

regions = ['us-east-1']

#instances = ec2.instances.filter#    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
running = {}
for item in regions:
        ec2 = boto3.resource('ec2',region_name=item)
        print("Listing instances in " + item)
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

        for instance in instances:

           # print("\n")
            print(instance.id, instance.private_dns_name)
            for tag in instance.tags:
                print tag
                    #running[instance.id] = instance.private_dns_name
#    instance.stop()

# print running

# invfile=open("inventory/ansible-nodes", "a")

# for key in running:
#     invfile.writelines("%s ansible_host=%s\n" % (key, running[key]))