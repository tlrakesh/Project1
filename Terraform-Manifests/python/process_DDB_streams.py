import json
import boto3
from pprint import pprint


def lambda_handler(event, context):
   for rec in event['Records']:
    print(type(rec))
    print(rec['eventName'])
    print(rec["dynamodb"])
    if rec['eventName'] == "INSERT":
		#Send a message to subsribers in sns topic
        try:
            topic_arn = "arn:aws:sns:us-east-2:170075111040:public-snapshot-details-from-ddb"
            client = boto3.client(service_name = "sns", region_name = "us-east-2")
            msg = str(rec)
            result = client.publish(TopicArn=topic_arn, Message=msg, Subject="dynamodb insert")
            print(result)
            if result['ResponseMetadata']['HTTPStatusCode'] == 200:
                print(result)
                print("Notification send successfully..!!!")
        except Exception as e:
           print("Error occured while publish notifications and error is : ", e)
