import json
import base64
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Extract data from the event
    try:

        file_name = event["queryStringParameters"]["file"]
         
        # Upload to S3
        """ URL = s3.generate_presigned_url(
            ClientMethod='put_object',
            Params={
                'Bucket': "uploadbucket653487us",
                'Key': file_name
            },
            ExpiresIn=3600
        )"""
        
        URL  = s3.generate_presigned_post(
            Bucket = "uploadbucket653487us",
            Key = file_name,
            Fields = None,
            Conditions = None,
            ExpiresIn = 3600
        )

        
        return {
            'statusCode': 200,
            'body': json.dumps({"URL":URL})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Missing key in request: {str(e)}")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"An error occurred: {str(e)}")
        }
