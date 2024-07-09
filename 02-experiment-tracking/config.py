AWS_S3_BUCKET_NAME = 'mlflow-artifact-remote-eff'
AWS_RDS_DATABASE_NAME = 'mlflow_db'
AWS_RDS_USERNAME = 'mlflow'
AWS_RDS_PASSWORD = 'lLrygNRfi4aZ9VObAwBe'
AWS_RDS_HOSTNAME = 'mlflow-database.c9kwaw2cy9ep.eu-north-1.rds.amazonaws.com'


AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
REGION_NAME = 'eu-north-1'
AWS_URL = 'mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri postgresql://DB_USER:DB_PASSWORD@DB_ENDPOINT:5432/DB_NAME --default-artifact-root s3://S3_BUCKET_NAME'