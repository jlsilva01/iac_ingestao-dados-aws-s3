provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-jorge"
    key    = "state/igti/edc/mod4/terraform.tfstate"
    region = "us-east-1"
  }
}