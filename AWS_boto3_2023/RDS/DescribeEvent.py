import boto3
from pprint import pprint
from datetime import datetime

rds_client=boto3.client('rds')

paginator = rds_client.get_paginator('describe_events')

response_iterator = paginator.paginate(

            Duration=123 
            )
print(response_iterator)
for response in response_iterator:
    for event in response['Events']:
        pprint(event)