import os

AWS_ACCESS_KEY_ID=os.environ.get("S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME= os.environ.get("S3_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL="https://s3.ir-thr-at1.arvanstorage.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION="https://s3.ir-thr-at1.arvanstorage.com"
DEFAULT_FILE_STORAGE = "core.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = 'core.cdn.backends.StaticRootS3BotoStorage'
