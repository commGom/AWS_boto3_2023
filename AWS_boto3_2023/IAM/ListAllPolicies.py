import boto3

def list_policies():
    iam=boto3.client('iam')
    
    paginator=iam.get_paginator('list_policies')
    total_cnt=0
    # Scope="AWS"
    # Scope="Local"
    for response in paginator.paginate(Scope="AWS"):
        print(len(response['Policies']))
        total_cnt+=len(response['Policies'])
        for policy in response['Policies']:
            policy_name=policy['PolicyName']
            Arn=policy['Arn']
            
            print('Policy Name : {} Arn : {}'.format(policy_name,Arn))
    print(total_cnt)
list_policies()