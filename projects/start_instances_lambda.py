import boto3

ec2 = boto3.client('ec2', region_name="us-east-1")
dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

def listInstances():   # **kwargs
    
    """ This listing the ec2 instances"""
    try: 
        response = ec2.describe_instances(Filters=[dev_filter])
        instance_list = []
        for instance in response['Reservations']:
            instance_id = instance['Instances'][0]['InstanceId']
            instance_list.append(instance_id)

        return instance_list
    except Exception as e:
        print(f"ERROR: {e}")

def startInstances(instance_list):
    try:
        ec2.start_instances(InstanceIds=instance_list)
        print("Instance started successfully...")
    except Exception as e:
        print(f"Error: {e}")


s = listInstances()
startInstances(s)
    
