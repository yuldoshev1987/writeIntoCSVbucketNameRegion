import boto as boto
import boto3
import csv
def getBucketNameAndRegion():
    s3_client = boto3.client('s3')
    s3_buckets=list()
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        temp=dict()
        bucket_name = (bucket["Name"])
        location_req=s3_client.get_bucket_location(Bucket=bucket_name)
        s3_location=location_req.get('LocationConstraint')
        if s3_location is None:
            s3_location='us-east-1'
        print('Bucket Name:',bucket_name,'Region:',s3_location)
        temp['S3_Name']=bucket_name
        temp['S3_location']=s3_location
        s3_buckets.append(temp)
    return s3_buckets
def writeIntoCSV(fileName,s3_buckets):
    with open(fileName,'w',newline='')as file:
        w=csv.writer(file)
        w.writerow(['BucketName','Region'])
        for i in s3_buckets:
            w.writerow([i.get('S3_Name'),i.get('S3_location')])

s3_buckets=getBucketNameAndRegion()
writeIntoCSV('s3_buckets.csv',s3_buckets)