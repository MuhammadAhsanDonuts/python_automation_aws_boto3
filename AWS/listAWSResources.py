# THIS SCRIPT IS GOING TO LIST THE SPEICIFIED RESOURCES, CAN ADD MORE IF NEEDED. 
# DEVELOPED BY AHSAN SHAIKH


import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

