import boto as boto
import boto3
import csv
import os
s3_client = boto3.client('s3')


def get_location(client, bucket_name):
    response = client.get_bucket_location(Bucket=bucket_name)
    return response['LocationConstraint']


# Specifies the Region where the bucket resides. For a list of all the Amazon S3 supported location constraints
# by Region, see Regions and Endpoints . Buckets in Region us-east-1 have a LocationConstraint of null

def write_bucketName_Region(s3_client,fileName):
    with open(fileName,'w',newline='')as f:
        w = csv.writer(f)  # returns writer object to write data
        w.writerow(['BucketName', 'Region'])
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            BucketName = (bucket["Name"])
            location = get_location(s3_client, BucketName)
            if location == None:
                location = 'us-east-1'
            w.writerow([BucketName,location])
            print('Bucket Name:', BucketName, 'Region:', location)

write_bucketName_Region(s3_client,'s3BucketRegion.csv')


