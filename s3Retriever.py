import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = "uploadbucket653487"  # Replace with your bucket name
    try:
        # List all objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        # Extract object details
        objects = []
        if 'Contents' in response:
            for obj in response['Contents']:
                object_details = {
                    'Key': obj['Key'],
                    'LastModified': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S'),  # Format date
                    'Size': obj['Size']  # Size in bytes
                }
                objects.append(object_details)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Enable CORS for the frontend
            },
            'body': json.dumps({'objects': objects})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
