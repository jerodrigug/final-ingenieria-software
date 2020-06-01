import boto3

import config

s3_client = boto3.client('s3', aws_access_key_id=config.S3_ACCESS_KEY_ID, aws_secret_access_key=config.S3_SECRET_ACCESS_KEY, aws_session_token=config.S3_SESSION_TOKEN)

def upload_file_to_s3(file, acl='public-read'):
	try:
		s3_client.upload_fileobj(file, config.S3_BUCKET_NAME, file.filename, ExtraArgs={"ACL": acl, "ContentType": file.content_type})

	except Exception as e:
		print("Something Happened: ", e)
		return e

	return "{}{}".format(config.S3_LOCATION, file.filename)