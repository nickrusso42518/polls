"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: AWS Lambda function to run the RCP poll
collector in a serverless fashion.
"""

import boto3
import polls


def lambda_handler(event, context):
    """
    AWS Lambda function that collects the RCP averages and writes
    the HTML text to the index.html file at http://polls.njrusmc.net
    for easy viewing.
    """

    print("S3 upload started")

    # Create a reference to the S3 server and collect
    # the RCP polling averages specified in the JSON file
    s3 = boto3.client("s3")
    html_text = polls.get_rcp_averages("elections.json")

    # Print the HTML text as confirmation
    print(html_text)

    # Create a byte collection of the HTML text as UTF-8
    upload_bytes = bytes(html_text.encode("UTF-8"))

    # Upload the index.html file to the S3 bucket
    s3.put_object(
        Bucket="polls.njrusmc.net",
        Key="index.html",
        ContentType="text/html",
        Body=upload_bytes,
    )

    # Print final status message indicating success
    print("S3 upload complete")
