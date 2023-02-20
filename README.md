"# AWS_boto3_2023" 

# Preparation
- IAM 계정 (Console Login X 및 ReadOnly Access 권한 부여, Access Key 발급)
- AWS CLI 설치 (aws configure에 해당 IAM 계정 access key 정보 기입)

# What is boto3
- Description : AWS SDK for a python programming language, which allows python developers to write software that makes use of services
- Link : https://boto3.amazonaws.com/v1/documentation/api/latest/index.html 
- install boto3 library
```
pip install boto3
```
- configuration (AWS CLI : https://aws.amazon.com/ko/cli/)
```
pip install awscli
aws configure
```

## IAM
- User List
- Policy List

## RDS (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html?highlight=rds%20event#RDS.Paginator.DescribeEvents)
- DescribeRDS (DBIdentifier로 filter or 전체 리스트)
- DescribeEvents (이벤트 기록 확인)
- DescribeDBLogFiles (DB 로그 파일 목록)