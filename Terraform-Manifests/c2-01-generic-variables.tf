variable "aws_region" {
    description = "Region for the resources"
    type = string
    default = "us-east-2" 
}

variable "environment" {
    description = "indicates dev-test-prod environment"
    type = string
    default = "dev"
}

variable "business_division" {
    description = "for which department these resources are being created"
    type = string
    default = "HR" 
}

variable "bucket_name" {
    description = "Bucket name"
    type = string
    default = "my-tf-rtl-bucket"
  
}