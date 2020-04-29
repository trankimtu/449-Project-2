web1: gunicorn3 -b localhost:$PORT --access-logfile - api:app
# web2: gunicorn3 -b localhost:$PORT --access-logfile - votes:app
db: java -Djava.library.path=./dynamodb_local_latest/DynamoDBLocal_lib -jar dynamodb_local_latest/DynamoDBLocal.jar -sharedDb


