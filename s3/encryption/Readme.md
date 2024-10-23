## Create a bucket

aws s3 mb s3://encryption-fun-jpm-12313

## Create a file

echo "Hello World" > hello.txt
aws s3 cp hello.txt s3://encryption-fun-jpm-12313

## Put object with encryption of KMS

aws s3api put-object \
--bucket encryption-fun-jpm-12313 \
--key hello.txt \
--body hello.txt \
--server-side-encryption aws:kms \
--ssekms-key-id "key"

### Put Object with SSE-C

BASE64_ENCODED_KEY=$(openssl rand -base64 32)

echo $BASE64_ENCODED_KEY

export MD5_VALUE=$(echo -n $BASE64_ENCODED_KEY | md5sum | awk '{print $1}' | base64 -w0)
echo -n 
aws s3api put-object \
--bucket encryption-fun-jpm-12313 \
--key hello.txt \
--body hello.txt \
--sse-customer-algorithm AES256 \
--sse-customer-key $BASE64_ENCODED_KEY \
--sse-custumer-md5 $MD5_VALUE