## Create a bucket
aws s3 mb s3://cors-fun-jpm-241332

## Change block public access
```sh
aws s3api put-public-access-block \
    --bucket cors-fun-jpm-241332 \
    --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```
## Create a bucket policy
aws s3api put-bucket-policy --bucket cors-fun-jpm-241332 --policy file://policy.json

## Turn on static website hosting

aws s3api put-bucket-website --bucket cors-fun-jpm-241332 --website-configuration file://website.json

## Upload our index.html file and include a resource that would be cross-origin

aws s3 cp index.html s3://cors-fun-jpm-241332

## Apply a CORS policy