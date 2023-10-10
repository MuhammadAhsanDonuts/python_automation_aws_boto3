import boto3

session = boto3.Session()

def get_instance_name(tags):
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'N/A'

def list_ec2_instances():
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    
    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            instance_name = get_instance_name(instance.get('Tags', []))
            instances.append([instance_id, instance_name, instance_type, state])

    return instances

ec2_data = list_ec2_instances()


if ec2_data:
    headers = ["Instance ID", "Name", "Instance Type", "State"]

    from tabulate import tabulate
    table = tabulate(ec2_data, headers=headers, tablefmt="pretty")
    print(table)
else:
    print("No EC2 instances found.")
