import boto3
from pprint import pprint

def describe_rdsInfo(DBInstanceIdentifier):
    rds_client=boto3.client('rds')

    response=rds_client.describe_db_instances(
        DBInstanceIdentifier=DBInstanceIdentifier
    )
    pprint(response)

# DBInstanceIdentifier='database-1'
# describe_rdsInfo(DBInstanceIdentifier)

def list_rdsInfo():
    rds_client=boto3.client('rds')
    
    response=rds_client.describe_db_instances()
    
    for db in response["DBInstances"]:
        pprint(db)
        
list_rdsInfo()