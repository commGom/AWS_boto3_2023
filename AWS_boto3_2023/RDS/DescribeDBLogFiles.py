import boto3

rds_client=boto3.client('rds')

paginator = rds_client.get_paginator('describe_db_log_files')

response_iterator = paginator.paginate(
    DBInstanceIdentifier='database-1'
)

for response in response_iterator:
    print(response)