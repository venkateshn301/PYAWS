import boto3
import pandas as pd
# AWS credentials configuration
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIARNRBYV5VRJ3T2XPU',
    aws_secret_access_key='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')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
###################################
import csv
# Loading csv file into s3 bucket
data1={'Name':['Venkat','Naresh','Chenchaiah','Varalu','Jayanthi'],
        'Age':[28,26,55,45,30]}
family=pd.DataFrame(data1)        
# Generating csv file
family.to_csv('family.csv')

#Uploading csv file to s3
s3.Bucket('boto3awss3').upload_file(Filename='family.csv',Key='MyFamily1.csv')

list=[]
# List bucket objects here
for file in s3.Bucket('boto3awss3').objects.all():
    list.append(str(file))
print(list)

#Downloading files from S3
s3.Bucket('boto3awss3').download_file(Key='MyFamily.csv',Filename='sample.csv')
df=pd.read_csv('sample.csv',index_col=0)

print(df)