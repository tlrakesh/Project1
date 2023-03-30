resource "aws_sqs_queue" "snapshots_queue" {
  name                      = "snapshots-queue"
  delay_seconds             = 90
  max_message_size          = 256000
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  /*
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.snapshot_queue_deadletter.arn
    maxReceiveCount     = 4
  })
  */

  tags = local.common_tags
}
