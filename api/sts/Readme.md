## Create a user with no permissions

```sh
aws iam create-user --user-name sts-machine-user
aws iam create-access-key --user-name sts-machine-user --output table
```

## Create a Role

We need to create a role that will access a new resource

```sh
chmod u+x bin/deploy
./bin/deploy
```

## Use new user credentials and assume role
aws sts assume-role \
    --role-arn arn:aws:iam::903437509637:role/my-sts-fun-stack-StsRole-4YY8OTUl7oab \
    --role-session-name assume-role-s3 \
    --profile sts

    