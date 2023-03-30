output "Lambda_role_arn" {
    description = "Lambda iam role arn"
    value = aws_iam_role.lambda_role.arn  
}

output "Lambda_role_assume_roles" {
    description = "Lambda iam role assume policies"
    value = aws_iam_role.lambda_role.assume_role_policy
}

output "Lambda_role_permissions_boundary" {
    description = "Lambda iam role permissions boundary"
    value = aws_iam_role.lambda_role.permissions_boundary
}

output "lambda_csv_to_S3_handler_name" {
    description = "Lambda handler name"
    value = aws_lambda_function.Lambda_from_terraform_to_upload_csv_to_s3
}
output "lambda_S3_to_SQS_handler_name" {
    description = "Lambda handler name"
    value = aws_lambda_function.Lambda_process_SQS_event
}
output "lambda_SQS_to_DDB_handler_name" {
    description = "Lambda handler name"
    value = aws_lambda_function.Lambda_process_SQS_event
}

