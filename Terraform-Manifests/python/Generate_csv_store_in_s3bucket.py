''' 
This Lambda function creates a csv and stores it in S3 using below steps.
----Using ec2 client get the public snapshot details shown below.
----id,Description,Encrypted,OwnerId,Progress,SnapshotId,StartTime,State,VolumeId,VolumeSize,StorageTier
----Store the details in S3 in csv file format  
---- Also creates a Dynamo DB table after csv is written successfuly into S3. Table is only created when it does nopt exist already.
** More Pointers **
 * Used Paginators and Waiters *
'''
import boto3
from pprint import pprint
import csv
import pandas as pd
import io

def lambda_handler(event, context):
    # TODO implement
    #aws_console_session = boto3.session.Session(profile_name="admin")
    # ec2_console_res = aws_console_session.resource(service_name="ec2",region_name = "us-east-2")
    #ec2_console_client = aws_console_session.client(service_name="ec2", region_name="us-east-2")
    ec2_console_client = boto3.client(service_name="ec2",region_name = "us-east-2")
    s3_client = boto3.client(service_name="s3")
    waiter = s3_client.get_waiter('object_exists')
    max_res = 10
    cnt = 1
    #csv_ob = open("snapshots_info.csv", "w", newline='')
    #csv_w = csv.writer(csv_ob)
    StartTime = ''
    remove_commas_in_description = ''
    key_names = []
    key_values = []
    actual_row = {}
    sno_values = []
    StartTime = ''
    remove_commas_in_description = ''
    key_names = ["cnt"]
    key_values = []
    actual_row = {}
    csv_file_name = "snapshot-details.csv"
    Description_values = []
    Encrypted_values = []
    OwnerId_values = []
    Progress_values = []
    SnapshotId_values = []
    StartTime_values = []
    State_values = []
    VolumeId_values = []
    VolumeSize_values = []
    StorageTier_values = []
    id_values = []
    bucket_name = "my-tf-rtl-bucket"
    ddb_table_name = "public_snapshot_details"
    """
    for each_snap in ec2_console_res.snapshots.all():
        print(each_snap.id)
    """
    # For each snap shot object prepare a row.
    for each_snap_shot_obj in ec2_console_client.describe_snapshots(MaxResults=max_res)['Snapshots']:
        id_values.append(cnt)
        if cnt == 1:
            key_names.append(each_snap_shot_obj.keys())
        for each_key in each_snap_shot_obj:
            #sno_values.append(cnt)
            if each_key == "Description":
                 Description_values.append(each_snap_shot_obj[each_key].replace(",", ""))
            if each_key == "Encrypted":
                 Encrypted_values.append(each_snap_shot_obj[each_key])
            if each_key == "OwnerId":
                 OwnerId_values.append(each_snap_shot_obj[each_key])
            if each_key == "Progress":
                 Progress_values.append(each_snap_shot_obj[each_key])
            if each_key == "SnapshotId":
                 SnapshotId_values.append(each_snap_shot_obj[each_key])
            if each_key == "StartTime":
                 StartTime_values.append(each_snap_shot_obj[each_key].strftime("%Y-%m-%d"))
            if each_key == "State":
                 State_values.append(each_snap_shot_obj[each_key])
            if each_key == "VolumeId":
                 VolumeId_values.append(each_snap_shot_obj[each_key])
            if each_key == "VolumeSize":
                 VolumeSize_values.append(each_snap_shot_obj[each_key])
            if each_key == "StorageTier":
                 StorageTier_values.append(each_snap_shot_obj[each_key])
        cnt = cnt + 1
    csv_data_dict = {
          "id" : id_values,
          "Description" : Description_values,
          "Encrypted": Encrypted_values,
          "OwnerId": OwnerId_values,
          "Progress": Progress_values,
          "SnapshotId":SnapshotId_values,
          "StartTime":StartTime_values,
          "State":State_values,
          "VolumeId":VolumeId_values,
          "VolumeSize":VolumeSize_values,
          "StorageTier":StorageTier_values
    }
    csv_data_frame = pd.DataFrame(csv_data_dict)
    #csv_file_name = "snapshot-details.csv"
    #csv_data_frame.to_csv(csv_file_name,index=False)
    with io.StringIO() as csv_buffer:
        csv_data_frame.to_csv(csv_buffer, index=False)
        response = s3_client.put_object(
        Bucket=bucket_name, Key="snapshot-details.csv", Body=csv_buffer.getvalue()
        )
        waiter.wait(
             Bucket=bucket_name,
             Key="snapshot-details.csv",
             WaiterConfig={
             'Delay': 300,
             'MaxAttempts': 123
             }
             )
        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        if status == 200:
            print(f"Successful S3 put_object response. Status - {status}")
            # check if already exists and Create a dynamodb table to store csv details.
            ddb_table_name = "public_snapshot_details"
            ddb_client = boto3.client(service_name="dynamodb",region_name = "us-east-2")
            ddb_resource = boto3.resource(service_name="dynamodb",region_name = "us-east-2")
            paginator = ddb_client.get_paginator('list_tables')
            response_iterator = paginator.paginate(
                 PaginationConfig={
                 'MaxItems': 100,
                 'PageSize': 100,
                 'StartingToken': 'page'
                 }
                 )
            list_of_tables = []
            for page in response_iterator:
                 for item in page['TableNames']:
                      list_of_tables.append(item)
                      #id,Description,Encrypted,OwnerId,Progress,SnapshotId,StartTime,State,VolumeId,VolumeSize,StorageTier
                      # #print(response_iterator)
                      print(list_of_tables)
            if ddb_table_name in list_of_tables:
                 print(f"table {ddb_table_name} already exists" )
            else:
                 ddb_resource.create_table(
                      TableName=ddb_table_name,
                      StreamSpecification={
                      'StreamEnabled' : True,
                      'StreamViewType' : 'NEW_IMAGE' 
                      },
                      KeySchema=[
                      {'AttributeName': 'id', 'KeyType': 'HASH'},
                      {'AttributeName': 'SnapshotId', 'KeyType': 'RANGE'},
                      ],
                      AttributeDefinitions=[
                      {'AttributeName': 'id', 'AttributeType': 'N'},
                      {'AttributeName': 'OwnerId', 'AttributeType': 'S'},
                      {'AttributeName': 'SnapshotId', 'AttributeType': 'S'},
                      ],
                      LocalSecondaryIndexes=[
                      {
                      'IndexName': 'Index_id_ownerId',
                      'KeySchema': [
                      {'AttributeName': 'id','KeyType': 'HASH'},
                      {'AttributeName': 'OwnerId','KeyType': 'RANGE'},
                      ],
                      'Projection': {'ProjectionType': 'ALL',}
                      },
                      ],
                      ProvisionedThroughput={
                      'ReadCapacityUnits': 10,
                      'WriteCapacityUnits': 10
                      }
                    )
                 table_waiter = ddb_resource.meta.client.get_waiter('table_exists')
                 table_waiter.wait(
                      TableName=ddb_table_name,
                      WaiterConfig={
                      'Delay': 123,
                      'MaxAttempts': 123
                      }
                      )
        else:
            print(f"Unsuccessful S3 put_object response. Status - {status}")