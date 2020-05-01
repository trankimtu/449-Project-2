web1: gunicorn3 -b localhost:5000 --access-logfile - api:app
db: java -Djava.library.path=./dynamodb_local_latest/DynamoDBLocal_lib -jar dynamodb_local_latest/DynamoDBLocal.jar -sharedDb