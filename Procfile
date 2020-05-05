web1: gunicorn3 -b localhost:5000 --access-logfile - api:app
web2: gunicorn3 -b localhost:5100 --access-logfile - redisvotes:app
web3: gunicorn3 -b localhost:5200 --access-logfile - rss:app
db: java -Djava.library.path=./dynamodb_local_latest/DynamoDBLocal_lib -jar dynamodb_local_latest/DynamoDBLocal.jar -sharedDb
