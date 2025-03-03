import boto3

minio_client = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="epsi",
    aws_secret_access_key="epsi2024@"
)

bucket_name = "data-lake"

try:
    minio_client.create_bucket(Bucket=bucket_name)
except:
    pass

with open("vgsales.csv", "rb") as data:
    minio_client.put_object(Bucket=bucket_name, Key="raw/vgsales.csv", Body=data)

print("✅ Données envoyées dans MinIO !")
