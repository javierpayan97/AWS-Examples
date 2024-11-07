##NACL

```sh
aws ec2 create-network-acl --vpc-id vpc-0d22b3a47d889498f
```

187.250.201.11

## Get AMI for Amazon Linux 2
```sh
aws ec2 describe-images \
--owners amazon \
--filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
--query "Images[?starts_with(Name,'amzn2')]|sort_by(@, &CreationData)[-1].ImageId" \
--output text
```

## Add entry
```sh
aws ec2 create-network-acl-entry \
--network-acl-id acl-0ffa8c3c9a2a5a204 \
--ingress --rule-number 91 \
--protocol -1 \
--port-range From=0,To=65535 \
--cidr-block 200.60.221.100/32 \
--rule-action deny
```

```sh
aws ec2 describe-images \
    --owners amazon \
    --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
    --query "Images[*].[ImageId,CreationDate]" \
    --output text | sort -k2 -r | head -n 1
```
