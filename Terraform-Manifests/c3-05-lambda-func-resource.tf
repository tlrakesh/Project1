# This file have two lambda resurces.data "
# 1st is for creating csv and writing it into S3 bucket." 
# second is triggering a lambda from s3 to convert csv records into json msgs to SQS


resource "aws_lambda_function" "Lambda_from_terraform_to_upload_csv_to_s3" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "${path.module}/python/Generate_csv_store_in_s3bucket.zip"
  function_name = "tf_lambda_create_csv_pub_s3bucklet"
  role          = aws_iam_role.lambda_role.arn
  handler       = "Generate_csv_store_in_s3bucket.lambda_handler"
  source_code_hash = data.archive_file.Zip_csv_code.output_base64sha256
  runtime = "python3.9"
  layers = [
    "arn:aws:lambda:us-east-2:336392948345:layer:AWSSDKPandas-Python39:4"
  ]
  depends_on = [
    aws_iam_role_policy_attachment.Lambda_logs_policy_attachment,
    #aws_iam_role_policy_attachment.ec2_full_access_policy_attachment,
    aws_iam_role_policy_attachment.ec2_describe_snapshots_policy_attachment,
    aws_iam_role_policy_attachment.bucket_policy_attachment,
    aws_iam_role_policy_attachment.ddb_policy_attachment,
    #aws_iam_role_policy_attachment.ddb_createtable_policy_attachment,
    aws_iam_role.lambda_role,
    aws_s3_bucket.tf_bucket,
  ]
  timeout = 600
  memory_size = 256
  }


resource "aws_lambda_function" "Lambda_trigger_from_s3_to_SQS" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "${path.module}/python/post_csv_content_from_s3_to_sqs.zip"
  function_name = "tf_lambda_send_s3_csv_content_to_sqs"
  role          = aws_iam_role.lambda_role.arn
  handler       = "post_csv_content_from_s3_to_sqs.lambda_handler"
  source_code_hash = data.archive_file.Zip_s3_sqs_code.output_base64sha256
  runtime = "python3.9"
  layers = [
    "arn:aws:lambda:us-east-2:336392948345:layer:AWSSDKPandas-Python39:4"
  ]
  depends_on = [
    aws_iam_role_policy_attachment.Lambda_logs_policy_attachment,
    #aws_iam_role_policy_attachment.ec2_full_access_policy_attachment,
    aws_iam_role_policy_attachment.ec2_describe_snapshots_policy_attachment,
    aws_iam_role_policy_attachment.bucket_policy_attachment,
    aws_iam_role_policy_attachment.ddb_policy_attachment,
    aws_iam_role.lambda_role,
    aws_s3_bucket.tf_bucket,
  ]
  timeout = 600
  memory_size = 256
  }


  resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.Lambda_trigger_from_s3_to_SQS.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.tf_bucket.arn
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.tf_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.Lambda_trigger_from_s3_to_SQS.arn
    events              = ["s3:ObjectCreated:*","s3:ObjectRemoved:*"]
    filter_suffix       = ".csv"
  }

  depends_on = [aws_lambda_permission.allow_bucket]
}




resource "aws_lambda_function" "Lambda_process_SQS_event" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "${path.module}/python/process_SQS_event.zip"
  function_name = "tf_process_SQS_event_to_dynamodb"
  role          = aws_iam_role.lambda_role.arn
  handler       = "process_SQS_event.lambda_handler"
  source_code_hash = data.archive_file.Zip_SQS_Ddb_code.output_base64sha256
  runtime = "python3.9"
  layers = [
    "arn:aws:lambda:us-east-2:336392948345:layer:AWSSDKPandas-Python39:4"
  ]
  depends_on = [
    aws_iam_role_policy_attachment.Lambda_logs_policy_attachment,
    #aws_iam_role_policy_attachment.ec2_full_access_policy_attachment,
    aws_iam_role_policy_attachment.ec2_describe_snapshots_policy_attachment,
    aws_iam_role_policy_attachment.bucket_policy_attachment,
    aws_iam_role_policy_attachment.ddb_policy_attachment,
    aws_iam_role.lambda_role,
    aws_s3_bucket.tf_bucket,
    aws_sqs_queue.snapshots_queue,
  ]
  timeout = 600
  memory_size = 256
  }

resource "aws_lambda_event_source_mapping" "SQS_Lambda_mapping" {
  event_source_arn = aws_sqs_queue.snapshots_queue.arn
  enabled = true
  function_name    = aws_lambda_function.Lambda_process_SQS_event.arn
  batch_size = 1
  depends_on = [aws_sqs_queue.snapshots_queue]
}


resource "aws_lambda_function" "process_DDB_streams" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "${path.module}/python/process_DDB_streams.zip"
  function_name = "tf_process_DDB_streams"
  role          = aws_iam_role.lambda_role.arn
  handler       = "process_DDB_streams.lambda_handler"
  source_code_hash = data.archive_file.Zip_Ddb_streams_code.output_base64sha256
  runtime = "python3.9"
  layers = [
    "arn:aws:lambda:us-east-2:336392948345:layer:AWSSDKPandas-Python39:4"
  ]
  depends_on = [
    aws_iam_role_policy_attachment.Lambda_logs_policy_attachment,
    #aws_iam_role_policy_attachment.ec2_full_access_policy_attachment,
    aws_iam_role_policy_attachment.ec2_describe_snapshots_policy_attachment,
    aws_iam_role_policy_attachment.bucket_policy_attachment,
    aws_iam_role_policy_attachment.ddb_policy_attachment,
    aws_iam_role_policy_attachment.sns_policy_attachment,
    aws_iam_role.lambda_role,
    aws_s3_bucket.tf_bucket,
    aws_sqs_queue.snapshots_queue,
  ]
  timeout = 600
  memory_size = 256
  }

resource "aws_lambda_event_source_mapping" "ddb_Lambda_mapping" {
  event_source_arn  = "arn:aws:dynamodb:us-east-2:170075111040:table/public_snapshot_details/stream/2023-03-22T20:18:20.098"
  function_name     = aws_lambda_function.process_DDB_streams.arn
  starting_position = "LATEST"
  enabled = true
}