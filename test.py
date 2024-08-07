import boto3

def publickBuckets(region):
    conn = boto3.client('s3', region_name=region)
    buckets = conn.list_buckets()
    bucket_list = []
    for b in buckets['Buckets']:
        bucket_list.append(b['Name'])
    public_bucket = []
    for bucket in bucket_list:   
        bucket_acl = conn.get_bucket_acl(Bucket=bucket)
        for item in bucket_acl.get('Grants'):
            grantees = item.get('Grantee')
            uri = grantees.get('URI','')
            if 'AllUsers' in uri:
                public_bucket.append(bucket)
                break
                
                
    return public_bucket       
        

import boto3

# Create an IAM service resource
iam = boto3.client('iam')
list_user = []
# List all IAM users
response = iam.list_users()
for user in response['Users']:
    user_name = user['UserName']
    list_user.append(user_name)
for usr in  list_user:
    keys_response = iam.list_access_keys(UserName=usr)
    for k in keys_response['AccessKeyMetadata']:
        print("userName:", user , k['AccessKeyId'], k['Status'])