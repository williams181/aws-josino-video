import boto3

def upload_file2(file, file_name):
    s3 = boto3.client('s3')
    s3.upload_file(file,'netflix-clone-josino', file_name)
    
def list_file1():
    session = boto3.Session( 
            aws_access_key_id='ASIA5NBMOBZQUMXUJKKZ', 
            aws_secret_access_key='ElPpO6hsCj3K4jLh2U+5uhtRbsVEaLQgPlNvumFU')


    #Then use the session to get the resource
    s3 = session.resource('s3')

    my_bucket = s3.Bucket('netflix-clone-josino')

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)
