import json
import boto3
from pprint import pprint

pprint('Loading function')

def lambda_handler(event, context):
   event = {
      "Records":[{
         "eventID":"2248766b3d15525d91b87a84ce359eed",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-00eeaa5d6f3b02585"
               },
               "id":{
                  "N":"1"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-00eeaa5d6f3b02585"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-ffffffff"
               },
               "Description":{
                  "S":"Copied for DestinationAmi ami-fed7f49b from Source"
               },
               "OwnerId":{
                  "S":"605812595337"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2017-08-30"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"1"
               },
               "VolumeSize":{
                  "N":"8"
               }
            },
            "SequenceNumber":"4533200000000000430305246",
            "SizeBytes":258,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      ]
   }
   for rec in event['Records']:
    print(type(rec))
    print(rec['eventName'])
    print(rec["dynamodb"])
    if rec['eventName'] == "INSERT":
		#Send a message to subsribers in sns topic
        try:
            topic_arn = "arn:aws:sns:us-east-2:170075111040:public-snapshot-details-from-ddb"
            client = boto3.client(service_name = "sns", region_name = "us-east-2")
            result = client.publish(TopicArn=topic_arn, Message=str(rec), Subject="dynamodb insert")
            print(result)
            if result['ResponseMetadata']['HTTPStatusCode'] == 200:
                print(result)
                print("Notification send successfully..!!!")
        except Exception as e:
           print("Error occured while publish notifications and error is : ", e)

'''
event = {
   "Records":[
      {
         "eventID":"2248766b3d15525d91b87a84ce359eed",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-00eeaa5d6f3b02585"
               },
               "id":{
                  "N":"1"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-00eeaa5d6f3b02585"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-ffffffff"
               },
               "Description":{
                  "S":"Copied for DestinationAmi ami-fed7f49b from Source"
               },
               "OwnerId":{
                  "S":"605812595337"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2017-08-30"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"1"
               },
               "VolumeSize":{
                  "N":"8"
               }
            },
            "SequenceNumber":"4533200000000000430305246",
            "SizeBytes":258,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"db035d7dc66a8817dde7938782487eed",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-0f05a5c2eef0f9967"
               },
               "id":{
                  "N":"2"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-0f05a5c2eef0f9967"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-ffffffff"
               },
               "Description":{
                  "S":"Copied for DestinationAmi ami-efd4f78a from Source"
               },
               "OwnerId":{
                  "S":"605812595337"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2017-08-30"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"2"
               },
               "VolumeSize":{
                  "N":"8"
               }
            },
            "SequenceNumber":"4533300000000000430305258",
            "SizeBytes":258,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"bbdd5dea8eb8803cca8fbb47dbf22f3b",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-030bcc649e110e5d7"
               },
               "id":{
                  "N":"3"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-030bcc649e110e5d7"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-02ed2b869b87e4183"
               },
               "Description":{
                  "S":"Created by CreateImage(i-0354eab7b73f6bced) for am"
               },
               "OwnerId":{
                  "S":"971594493945"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-30"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"3"
               },
               "VolumeSize":{
                  "N":"8"
               }
            },
            "SequenceNumber":"4533400000000000430305261",
            "SizeBytes":267,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"98b718bf13283f6dcf0f651d21cc6c82",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-01f3808b52156b16f"
               },
               "id":{
                  "N":"4"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-01f3808b52156b16f"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-0fe4d9524b85993f5"
               },
               "Description":{
                  "S":"Created by CreateImage(i-09c201e28248e1edd) for am"
               },
               "OwnerId":{
                  "S":"971594493945"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-30"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"4"
               },
               "VolumeSize":{
                  "N":"8"
               }
            },
            "SequenceNumber":"4533500000000000430305262",
            "SizeBytes":267,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"ec358e0d49e8f50d3c7b39d867d64004",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-0ca7a90342dd87120"
               },
               "id":{
                  "N":"5"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-0ca7a90342dd87120"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-0419353cd3dcee97b"
               },
               "Description":{
                  "S":"Created by CreateImage(i-0e236b0125e77f9b9) for am"
               },
               "OwnerId":{
                  "S":"971594493945"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-30"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"5"
               },
               "VolumeSize":{
                  "N":"8"
               }
            },
            "SequenceNumber":"4533600000000000430305263",
            "SizeBytes":267,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"4b69d494f1028fb8fa38155fd47facfd",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-02df15cb945aab34a"
               },
               "id":{
                  "N":"6"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-02df15cb945aab34a"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-ffffffff"
               },
               "Description":{
                  "S":"Copied for DestinationAmi ami-0ce2b78cc9d84a196 fr"
               },
               "OwnerId":{
                  "S":"462397596885"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-29"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"6"
               },
               "VolumeSize":{
                  "N":"3"
               }
            },
            "SequenceNumber":"4533700000000000430305264",
            "SizeBytes":258,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"905a8576caea15f9ee6bfa9f67e5b420",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-08f3b8ca21e025fc6"
               },
               "id":{
                  "N":"7"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-08f3b8ca21e025fc6"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-04696b8590f4e73f1"
               },
               "Description":{
                  "S":"devfile-64-9a69-59b2-devfile-32-9a69-59b2-devfile-"
               },
               "OwnerId":{
                  "S":"141523506793"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-29"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"7"
               },
               "VolumeSize":{
                  "N":"64"
               }
            },
            "SequenceNumber":"4533800000000000430305265",
            "SizeBytes":267,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"16ac88fb22ee2ab3bb74f38305e1fc29",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-0de5c5066ab2c7cf4"
               },
               "id":{
                  "N":"8"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-0de5c5066ab2c7cf4"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-ffffffff"
               },
               "Description":{
                  "S":"Copied for DestinationAmi ami-08e22dba279d56c63 fr"
               },
               "OwnerId":{
                  "S":"704708324783"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-28"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"8"
               },
               "VolumeSize":{
                  "N":"128"
               }
            },
            "SequenceNumber":"4533900000000000430305275",
            "SizeBytes":259,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"6f4e8dc8465b92ef212e9fc9f00377d5",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-07c2965299066171e"
               },
               "id":{
                  "N":"9"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-07c2965299066171e"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-0c03cb6292a816cfe"
               },
               "Description":{
                  "S":"devfile-64-50cd-4b15-devfile-32-50cd-4b15-devfile-"
               },
               "OwnerId":{
                  "S":"141523506793"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-28"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"9"
               },
               "VolumeSize":{
                  "N":"64"
               }
            },
            "SequenceNumber":"4534000000000000430305281",
            "SizeBytes":267,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      },
      {
         "eventID":"49a74aa96784c8be44ba5297ac3cdc28",
         "eventName":"INSERT",
         "eventVersion":"1.1",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-2",
         "dynamodb":{
            "ApproximateCreationDateTime":1679516648.0,
            "Keys":{
               "SnapshotId":{
                  "S":"snap-0a52eb77b7018dd27"
               },
               "id":{
                  "N":"10"
               }
            },
            "NewImage":{
               "SnapshotId":{
                  "S":"snap-0a52eb77b7018dd27"
               },
               "Progress":{
                  "S":"100%"
               },
               "VolumeId":{
                  "S":"vol-ffffffff"
               },
               "Description":{
                  "S":"Copied for DestinationAmi ami-073f82b73663734ef fr"
               },
               "OwnerId":{
                  "S":"462397596885"
               },
               "Encrypted":{
                  "BOOL":False
               },
               "State":{
                  "S":"completed"
               },
               "StartTime":{
                  "S":"2022-10-28"
               },
               "StorageTier":{
                  "S":"standard"
               },
               "id":{
                  "N":"10"
               },
               "VolumeSize":{
                  "N":"3"
               }
            },
            "SequenceNumber":"4534100000000000430305288",
            "SizeBytes":258,
            "StreamViewType":"NEW_IMAGE"
         },
         "eventSourceARN":"arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
      }
   ]
}


for rec in event['Records']:
	print(type(rec))
	if rec['eventName'] == "INSERT":
		#Send a message to subsribers in sns topic
		try:
			topic_arn = "arn:aws:sns:us-east-2:170075111040:public-snapshot-details-from-ddb"
			client = boto3.client(service_name = "sns", region_name = "us-east-2")
			result = client.publish(TopicArn=topic_arn, Message=rec, Subject="dynamodb insert")
			if result['ResponseMetadata']['HTTPStatusCode'] == 200:
				print(result)
				print("Notification send successfully..!!!")
		except Exception as e:
			print("Error occured while publish notifications and error is : ", e)
'''