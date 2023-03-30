data "archive_file" "Zip_csv_code" {
  type             = "zip"
  source_file      = "${path.module}/python/Generate_csv_store_in_s3bucket.py"
  output_file_mode = "0666"
  output_path      = "${path.module}/python/Generate_csv_store_in_s3bucket.zip"
}

data "archive_file" "Zip_s3_sqs_code" {
  type             = "zip"
  source_file      = "${path.module}/python/post_csv_content_from_s3_to_sqs.py"
  output_file_mode = "0666"
  output_path      = "${path.module}/python/post_csv_content_from_s3_to_sqs.zip"
}

data "archive_file" "Zip_SQS_Ddb_code" {
  type             = "zip"
  source_file      = "${path.module}/python/process_SQS_event.py"
  output_file_mode = "0666"
  output_path      = "${path.module}/python/process_SQS_event.zip"
}

data "archive_file" "Zip_Ddb_streams_code" {
  type             = "zip"
  source_file      = "${path.module}/python/process_DDB_streams.py"
  output_file_mode = "0666"
  output_path      = "${path.module}/python/process_DDB_streams.zip"
}