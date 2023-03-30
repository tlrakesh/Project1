#Policy/Permission for Lambda to get the list of snapshot details 
resource "aws_iam_policy" "lambda_snapshot_policy" {
  name        = "lambda-snapshot-policy"
  path        = "/"
  description = "AWS IAM policy for managing the lambda role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode(
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSnapshotTierStatus",
                "ec2:DescribeSnapshots",
                "ses:*"
            ],
            "Resource": "*"
        }
    ]
})
}

#Policy/Permission for Lambda to put and get the objects from S3. 
resource "aws_iam_policy" "lambda_bucket_permissions" {
  name        = "lambda-bucket-permissions"
  path        = "/"
  description = "AWS IAM policy for managing the lambda role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode(
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            #"Resource": ["arn:aws:s3:::lambda-to-s3-snapshot-details", "arn:aws:s3:::lambda-to-s3-snapshot-details/*",aws_s3_bucket.tf_bucket.arn]
            "Resource": "*"
        }
    ]
    #depends_on = [aws_s3_bucket.tf_bucket]
})
}



