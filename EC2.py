import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')
 

instances = ec2_resource.create_instances(
        ImageId='ami-0ddfba243cbee3768',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='mumbai_devopslearning_key',
        SecurityGroups=['launch-wizard-1'],
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'VolumeSize': 20,
                    'VolumeType': 'gp2',
                    'DeleteOnTermination': False,
                }
            }

        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Final_ec2_sever'
                    },
                ]
            }
        ],
        UserData='''#!/bin/bash
        # update the os
        sudo apt update -y
        #install Apache
        sudo apt install apache2 -y
        sudo systemctl start apache2
        # Enable Apache to start on boot
        sudo systemctl enable apache2
        # create sample index.html
        echo "<html><h1> Welcome to DevOps Learning </h1></html>" > /var/www/html/index.html

        # allow apache form the firewall
        sudo ufw allow 'Apache'
        ''', 
 )

print("instance created sucessfully")


    