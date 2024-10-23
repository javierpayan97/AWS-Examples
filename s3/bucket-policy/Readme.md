## Create a bucket
aws s3 mb s3://bucket-policy-example-jpm-24141

##

aws s3api put-bucket-policy --bucket "bucket-policy-example-jpm-24141" --policy file://policy.json

aws s3 rb s3://bucket-policy-example-jpm-24141