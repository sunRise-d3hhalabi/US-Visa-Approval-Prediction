import boto3
import os
from us_visa.constants import REGION_NAME


class S3Client:

    s3_client=None
    s3_resource = None
    def __init__(self, region_name=REGION_NAME):
        """ 
        This Class gets aws credentials from env_variable and creates an connection with s3 bucket 
        and raise exception when environment variable is not set
        """

        if S3Client.s3_resource==None or S3Client.s3_client==None:
            __access_key_id = os.getenv("aws_access_key_id")
            __secret_access_key = os.getenv("aws_secret_access_key")
            __region_name = os.getenv("region_name")

            if __access_key_id is None:
                raise Exception(f"Environment variable: aws_access_key_id is not not set.")
            if __secret_access_key is None:
                raise Exception(f"Environment variable: aws_secret_access_key is not set.")
            if __region_name is None:
                raise Exception(f"Environment variable: region_name is not set.")            

            S3Client.s3_resource = boto3.resource('s3',
                                            aws_access_key_id=__access_key_id,
                                            aws_secret_access_key=__secret_access_key,
                                            region_name=__region_name
                                            )
            S3Client.s3_client = boto3.client('s3',
                                        aws_access_key_id=__access_key_id,
                                        aws_secret_access_key=__secret_access_key,
                                        region_name=__region_name
                                        )
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client