#!/usr/bin/python

import boto3

regions = ['us-east-1']

#instances = ec2.instances.filter#    Filters=[{'Name': 'instance-state-name', $

running = {}

for item in regions:
        ec2 = boto3.resource('ec2',region_name=item)
        print("Listing instances in " + item)
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name$

        for instance in instances:

           # print("\n")
            print(instance.id, instance.private_dns_name)
            running[instance.id] = instance.private_dns_name
#    instance.stop()

print running
