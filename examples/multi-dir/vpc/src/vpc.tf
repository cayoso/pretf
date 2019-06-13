resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block
  tags = {
    Name        = "pretf-workspaces-multi-dir-${var.environment}"
    Environment = var.environment
  }
}