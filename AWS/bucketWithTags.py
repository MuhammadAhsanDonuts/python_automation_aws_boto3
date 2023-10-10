import boto3
from tabulate import tabulate


session = boto3.Session()


def list_s3_buckets():
    s3 = session.client('s3')
    response = s3.list_buckets()
    
    buckets_data = []


    item_id = 1

    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        try:
            tags_response = s3.get_bucket_tagging(Bucket=bucket_name)

            tags = tags_response['TagSet'] if 'TagSet' in tags_response else [{'Key': 'N/A', 'Value': 'N/A'}]

            buckets_data.append([item_id, bucket_name, tags])
            item_id += 1

        except Exception as e:
           buckets_data.append([item_id, bucket_name, tags])
           item_id += 1
           print(e)
    return buckets_data
        
   

s3_bucket_data = list_s3_buckets()


if s3_bucket_data:

    headers = ["Item ID", "Bucket Name", "Bucket Tags"]


    table = tabulate(s3_bucket_data, headers=headers, tablefmt="pretty")
    print(table)
else:
    print("No S3 buckets found.")
