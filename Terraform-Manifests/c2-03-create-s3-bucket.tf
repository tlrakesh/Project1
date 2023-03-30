resource "aws_s3_bucket" "tf_bucket" {
  bucket = var.bucket_name
  tags = "${local.common_tags}"
}

resource "aws_s3_bucket_acl" "tf_enable_private" {
  bucket = aws_s3_bucket.tf_bucket.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "tf_enable_versioning" {
  bucket = aws_s3_bucket.tf_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}