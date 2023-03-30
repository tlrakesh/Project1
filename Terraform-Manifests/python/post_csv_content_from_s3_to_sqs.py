import boto3
from pprint import pprint
import csv
import pandas as pd
import io
import json

'''
aws_console_session = boto3.session.Session(profile_name="admin")
pprint(event["Records"][0]['s3']['bucket']['name'])
pprint(event["Records"][0]['s3']['object']['key'])
bucket_name = event["Records"][0]['s3']['bucket']['name']
object_name = event["Records"][0]['s3']['object']['key']
s3_client = boto3.client(service_name="s3",region_name = "us-east-2")
sqs_client = boto3.client("sqs", region_name="us-east-2")


#waiter = s3_client.get_waiter('object_exists')
get_csv_response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
pprint(get_csv_response)
df = pd.read_csv(io.BytesIO(get_csv_response["Body"].read()))
print(df)
with io.StringIO() as json_buffer:
    df.to_json(json_buffer,indent=4,orient='records')
    response = sqs_client.send_message(QueueUrl="https://sqs.us-east-2.amazonaws.com/170075111040/snapshots-queue",
                                       MessageBody=json_buffer.getvalue()
                                       )
print(response)

#print('\n')
#print(df.shape)
file_reader = get_csv_response['Body'].read().decode("utf-8")
print(file_reader)
users = file_reader.split("\n")
print(users)
'''

def lambda_handler(event, context):
    # TODO implement
    # # aws_console_session = boto3.session.Session(profile_name="admin")
    # # ec2_console_res = aws_console_session.resource(service_name="ec2",region_name = "us-east-2")
    # #ec2_console_client = aws_console_session.client(service_name="ec2", region_name="us-east-2")
    # bucket_name = "lambda-to-s3-snapshot-details"
    pprint(event)
    #aws_console_session = boto3.session.Session(profile_name="admin")
    pprint(event["Records"][0]['s3']['bucket']['name'])
    pprint(event["Records"][0]['s3']['object']['key'])
    bucket_name = event["Records"][0]['s3']['bucket']['name']
    object_name = event["Records"][0]['s3']['object']['key']
    s3_client = boto3.client(service_name="s3",region_name = "us-east-2")
    sqs_client = boto3.client("sqs", region_name="us-east-2")
    #waiter = s3_client.get_waiter('object_exists')
    get_csv_response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
    print(get_csv_response)
    df = pd.read_csv(io.BytesIO(get_csv_response["Body"].read()))
    with io.StringIO() as json_buffer:
        df.to_json(json_buffer,indent=4,orient='records')
        response = sqs_client.send_message(QueueUrl="https://sqs.us-east-2.amazonaws.com/170075111040/snapshots-queue",
                                       MessageBody=json_buffer.getvalue()
                                       )
        print(response)
        print("/n print after response /n")