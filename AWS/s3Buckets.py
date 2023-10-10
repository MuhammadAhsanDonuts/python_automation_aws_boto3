import boto3
from tabulate import tabulate

session = boto3.Session()

def list_s3_buckets():
    s3 = session.client('s3')
    response = s3.list_buckets()
    buckets = []

    item_id = 1

    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        buckets.append([item_id, bucket_name])
        item_id += 1

    return buckets

buckets_data = list_s3_buckets()
if buckets_data:

    headers = ["Item ID", "S3 Bucket"]

    table = tabulate(buckets_data, headers=headers, tablefmt="pretty")
    print(table)
else:
    print("No S3 buckets found.")

