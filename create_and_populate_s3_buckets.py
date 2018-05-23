import boto
import boto3
import os
import boto.s3
import sys
from boto.s3.key import Key
import string
import random


class S3BucketProperties(object):
    def __init__(self,url=None):
        self.url = url

    def get_list_of_photos_from_local_directory(self):
        if not os.path.isdir(self.url):
            return("Error: Url is not a Directory")
        else:
            return os.listdir(self.url)

    def get_aws_credentials(self):
        return [os.environ.get('AWS_ACCESS_KEY_ID'), os.environ.get('AWS_SECRET_ACCESS_KEY')]

    def generate_unique_s3_bucket_name(self, size=20, chars=string.ascii_uppercase + string.digits):
        random_str = ''.join(random.choice(chars) for _ in range(size))
        return random_str.lower() + "sample-writing-bucket"



class CreateNewS3Bucket(object):

    def __init__(self,url=None):
        self.url = url
        self.properties = S3BucketProperties(self.url)
        list_of_aws_credentials = self.properties.get_aws_credentials()

        '''
         '''
        resultant_object_from_s3_connection = boto.connect_s3(list_of_aws_credentials[0],
            list_of_aws_credentials[1])
           


        bucket_name = self.properties.generate_unique_s3_bucket_name()

        bucket = resultant_object_from_s3_connection.create_bucket(bucket_name,
         location=boto.s3.connection.Location.DEFAULT)

        print("BUCKET", bucket)
        '''
         '''
        list_of_documents = self.properties.get_list_of_photos_from_local_directory()

        for photo in list_of_documents:
            a_document_file = self.url + '/' + photo
            k = Key(bucket)
            k.key = photo
            k.set_contents_from_filename(a_document_file,cb=None, num_cb=10)
           



if __name__ == '__main__':
    testfile = "writing"

    test_s3_props = S3BucketProperties(testfile)
    new_s3_bucket = CreateNewS3Bucket(testfile)
