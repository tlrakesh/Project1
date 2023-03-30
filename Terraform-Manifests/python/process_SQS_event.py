import boto3
from pprint import pprint
import csv
import pandas as pd
import io
import json

def lambda_handler(event, context):
      #aws_console_session = boto3.session.Session(profile_name="admin")
      event_data = event["Records"][0]['body']
      event_data = json.loads(event_data)
      pprint(event_data)
      Table_Name='public_snapshot_details'
      ddb_res = boto3.resource(service_name='dynamodb',region_name = "us-east-2")
      table = ddb_res.Table(Table_Name)
      for json_record in event_data:
        id = json_record["id"]
        Description = json_record["Description"]
        Encrypted = json_record["Encrypted"]
        OwnerId = str(json_record["OwnerId"])
        Progress = json_record["Progress"]
        SnapshotId = json_record["SnapshotId"]
        StartTime = json_record["StartTime"]
        State = json_record["State"]
        VolumeId = json_record["VolumeId"]
        VolumeSize = json_record["VolumeSize"]
        StorageTier = json_record["StorageTier"]

        print("Adding detail:", id, SnapshotId)

        response = table.put_item(
            Item={
                "id":id,
                "Description":Description[0:50],
                "Encrypted":Encrypted,
                "OwnerId":OwnerId,
                "Progress":Progress,
                "SnapshotId":SnapshotId,
                "StartTime":StartTime,
                "State":State,
                "VolumeId":VolumeId,
                "VolumeSize":VolumeSize,
                "StorageTier":StorageTier
                }
                )
        print(response)
        '''
event = {
   "Records":[
      {
         "messageId":"43c74275-391a-494e-b7e3-3a60d3593a81",
         "receiptHandle":"AQEB74FX0Xem9qY7+FuyvIXPBGOP7ewk7t7kpsaEToSPCwNK+wqMWO4a2AS4rRxnqMuY1Y+Q9cPM8dR7ykEjsF3A85Y5qOeP6lbx3qEYVpgmWr1SDlsMgo+fkQT9Th9Jq4mRC0QYisgBZUdvjzRBkxKklCaFzySJhJ2A4kqQaybKV1A9sHrGudFy6Cn1bUAj3Al4rpc71lhzaMNM6daV/A4JMUe4vVF0NyFGS3aTrBlyc+EiuLCeM0jh+U4jMkbyh0Tvp4YIblnUmSbDE+jNridRCuVD8LK1jAcV+H+nA8JcjOgqZLQ7WfexNufIWIqqXSlXi7IlvE0WVhFY4YztFXf/1ks6iLiMcSuJe2vUYdlhPPFPauW2QNShXJpbsrsb6w1hitEoFL9JrYF1kEZDoxxJCQ==",
         "body":"[\n    {\n        \"id\":1,\n        \"Description\":\"Copied for DestinationAmi ami-fed7f49b from SourceAmi ami-7f5b6f1f for SourceSnapshot snap-0dedde06afbcb4c29. Task created on 1504053693297.\",\n        \"Encrypted\":false,\n        \"OwnerId\":605812595337,\n        \"Progress\":\"100%\",\n        \"SnapshotId\":\"snap-00eeaa5d6f3b02585\",\n        \"StartTime\":\"completed\",\n        \"State\":\"completed\",\n        \"VolumeId\":\"vol-ffffffff\",\n        \"VolumeSize\":8,\n        \"StorageTier\":\"standard\"\n    },\n    {\n        \"id\":2,\n        \"Description\":\"Copied for DestinationAmi ami-efd4f78a from SourceAmi ami-9c5b6ffc for SourceSnapshot snap-01bb383197b7bfee4. Task created on 1504053658797.\",\n        \"Encrypted\":false,\n        \"OwnerId\":605812595337,\n        \"Progress\":\"100%\",\n        \"SnapshotId\":\"snap-0f05a5c2eef0f9967\",\n        \"StartTime\":\"completed\",\n        \"State\":\"completed\",\n        \"VolumeId\":\"vol-ffffffff\",\n        \"VolumeSize\":8,\n        \"StorageTier\":\"standard\"\n    },\n    {\n        \"id\":3,\n        \"Description\":\"Created by CreateImage(i-0354eab7b73f6bced) for ami-0615a504c0c89fed5\",\n        \"Encrypted\":false,\n        \"OwnerId\":971594493945,\n        \"Progress\":\"100%\",\n        \"SnapshotId\":\"snap-030bcc649e110e5d7\",\n        \"StartTime\":\"completed\",\n        \"State\":\"completed\",\n        \"VolumeId\":\"vol-02ed2b869b87e4183\",\n        \"VolumeSize\":8,\n        \"StorageTier\":\"standard\"\n    },\n    {\n        \"id\":4,\n        \"Description\":\"Created by CreateImage(i-09c201e28248e1edd) for ami-0297435f8d98b0dac\",\n        \"Encrypted\":false,\n        \"OwnerId\":971594493945,\n        \"Progress\":\"100%\",\n        \"SnapshotId\":\"snap-01f3808b52156b16f\",\n        \"StartTime\":\"completed\",\n        \"State\":\"completed\",\n        \"VolumeId\":\"vol-0fe4d9524b85993f5\",\n        \"VolumeSize\":8,\n        \"StorageTier\":\"standard\"\n    },\n    {\n        \"id\":5,\n        \"Description\":\"Created by CreateImage(i-0e236b0125e77f9b9) for ami-015a42dac17de2b27\",\n        \"Encrypted\":false,\n        \"OwnerId\":971594493945,\n        \"Progress\":\"100%\",\n        \"SnapshotId\":\"snap-0ca7a90342dd87120\",\n        \"StartTime\":\"completed\",\n        \"State\":\"completed\",\n        \"VolumeId\":\"vol-0419353cd3dcee97b\",\n        \"VolumeSize\":8,\n        \"StorageTier\":\"standard\"\n    },\n    {\n        \"id\":6,\n        \"Description\":\"Copied for DestinationAmi ami-0ce2b78cc9d84a196 from SourceAmi ami-03b57868d831748de for SourceSnapshot snap-03ba855990e54d522. Task created on 1667046718224.\",\n        \"Encrypted\":false,\n        \"OwnerId\":462397596885,\n        \"Progress\":\"100%\",\n        \"SnapshotId\":\"snap-02df15cb945aab34a\",\n        \"StartTime\":\"completed\",\n        \"State\":\"completed\",\n        \"VolumeId\":\"vol-ffffffff\",\n        \"VolumeSize\":3,\n        \"StorageTier\":\"standard\"\n    }\n]",
         "attributes":{
            "ApproximateReceiveCount":"1",
            "SentTimestamp":"1679444780187",
            "SenderId":"AROASPGKEH2AHF3N36YFY:tf_lambda_send_s3_csv_content_to_sqs",
            "ApproximateFirstReceiveTimestamp":"1679444870187"
         },
         "messageAttributes":{
            
         },
         "md5OfBody":"1fe816495edbc3480a097c3e50737f60",
         "eventSource":"aws:sqs",
         "eventSourceARN":"arn:aws:sqs:us-east-2:170075111040:snapshots-queue",
         "awsRegion":"us-east-2"
      }
   ]
}
'''