##NACL

```sh
aws ec2 create-network-acl --vpc-id vpc-0d22b3a47d889498f
```

## Get AMI for Amazon Linux 2
```sh
aws ec2 describe-images \
--owners amazon \
--filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
--query "Images[?starts_with(Name,'amzn2')]|sort_by(@, &CreationData)[-1].ImageId" \
--output text
```

```sh
aws ec2 describe-images \
    --owners amazon \
    --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
    --query "Images[*].[ImageId,CreationDate]" \
    --output text | sort -k2 -r | head -n 1
```
