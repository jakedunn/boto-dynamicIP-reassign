#!/bin/python
#
# dynamicIPSecurityGroup.py
# Simple script to adjust IP adresses which are allowed acesses via ssh to current system IP Adress.
# Obvious security flaw is compromise of IAM User credentials. or http://wtfismyip.com is down
# 
# Made for Matt by Jake.
#
# Absolutly No Warranty or gaurentee provided =]

import boto.ec2
import urllib
import json

#Define Connection Parameters
#IAMUser: DynamicIP-Reassigner

ec2_aws_access_key_id = '<YOUR ACCESS KEY ID>'
ec2_aws_secret_access_key = '<YOUR SECRET ACCESS KEY>'
aws_region = '<YOUR REGION>'    #Likely 'us-west-1' see link for list of regions: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html

#Name of Security Group you wish to edit
security_group = '<YOUR SECURITY GROUP>'

#Find out what your dynamic IP is.
ip_query = urllib.urlopen('http://wtfismyip.com/json').read()
ip = json.loads(ip_query)["YourFuckingIPAddress"] + "/32"

#Create Connection object.
conn = boto.ec2.connect_to_region(aws_region, 
		aws_access_key_id = ec2_aws_access_key_id,
		aws_secret_access_key = ec2_aws_secret_access_key)


#Loops through all your security groups, finds the one you want, finds tcp rules about port 22, and revokes.
groups = conn.get_all_security_groups()
for group in groups:
    if group.name == security_group:
    	for rule in group.rules:
        	if (int(rule.from_port) == 22) and (int(rule.to_port) == 22):
        		conn.revoke_security_group(group_name = security_group, ip_protocol = 'tcp', cidr_ip = rule.grants[0], from_port = 22, to_port = 22)

#Authorizes your new IP.        	
conn.authorize_security_group(group_name = security_group, ip_protocol = 'tcp', cidr_ip = ip, from_port = 22, to_port = 22)