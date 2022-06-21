# HCL - Hashicorp Configuration Language
# Linguagem declarativa

resource "aws_s3_bucket" "datalake" {
  # Parametros de configuracao do recurso escolhido
  bucket = "${var.base_bucket_name}-${var.environment}-${var.account_number}"

  lifecycle {
    ignore_changes = [server_side_encryption_configuration]
  }

  tags = {
    IES   = "IGTI"
    CURSO = "EDC"
  }
}

resource "aws_s3_object" "raw-zone" {
    bucket = "${var.base_bucket_name}-${var.environment}-${var.account_number}"
    acl    = "private"
    key    = "raw-zone/"
}

resource "aws_s3_object" "staging-zone" {
    bucket = "${var.base_bucket_name}-${var.environment}-${var.account_number}"
    acl    = "private"
    key    = "staging-zone/"
}

resource "aws_s3_object" "consumer-zone" {
    bucket = "${var.base_bucket_name}-${var.environment}-${var.account_number}"
    acl    = "private"
    key    = "consumer-zone/"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "config" {
  bucket = aws_s3_bucket.datalake.bucket

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}