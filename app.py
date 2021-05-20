#imports
import boto3
import os
import datetime
import schedule


#defaults
d_path="E:/Work"
d_interval=1
d_access_key_id="AKIA5DX6XXXXXXXXXXXX"
d_access_key="K88q568nSpqxm7lOOGX0enZwTqrBXXXXXXXXXXXX"
d_bucket_name="backup-from-comp951"

print("Hello,Welcome to the Backup Service ")
print("Provide Path to the directory else default is taken")
path=input()
path= d_path if path=="" else path
print("Enter Intervals to push")
interval=input()
interval= d_interval if interval=="" else interval
print("Enter Acccess key id to the account")
access_key_id=input()
access_key_id= d_access_key_id if access_key_id =="" else access_key_id
print("Enter Access Key")
access_key=input()
access_key= d_access_key if access_key =="" else access_key
print("Enter Bucket Name")
bucket_name=input()
bucket_name= d_bucket_name if bucket_name=="" else bucket_name


def upload_files(path):
    logs = open("logs.txt","a")
    logs.write(f"Backing up for path {path} at {datetime.datetime.now}\n")
    session =boto3.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=access_key
    )
    logs.write("Session Created Succsfully")
    s3=session.resource('s3')
    bucket=s3.Bucket("backup-from-comp951")
    logs.write(f"Bucket {bucket} opened\n")
    
    for subdir,dirs,files in os.walk(path):
        for file in files:
            full_path= os.path.join(subdir,file)
            logs.write(f"opening {full_path}\n")
            with open(full_path,'rb') as data:
                log = bucket.put_object(Key=full_path[len(path)+1:],Body=data)
                print(log)

schedule.every(interval).hours.do(upload_files(path))
while(True):
    schedule.run_pending()