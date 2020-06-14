import boto3
import polls

def lambda_handler(event, context):
    print("S3 upload started")

    s3 = boto3.client("s3")
    html_text = polls.get_rcp_averages("elections.json")

    upload_bytes = bytes(html_text.encode("UTF-8"))
    s3.put_object(
        Bucket="polls.njrusmc.net",
        Key="index.html",
        Body=upload_bytes
    )

    print(html_text)
    print("S3 upload complete")
