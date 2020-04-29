# cpsc449_microservices

## Steps to run: 
```sh
$ pip3 install --user Flask-API python-dotenv
$ pip3 install --user pugsql 
$ sudo apt install --yes ruby-foreman
```
```sh
$ flask init
```
```sh
$ foreman start
```
```sh
$ foreman start -m web1=<number of instances => 3>,web2=<number of instances => 3>,caddy=1
```

## Error: 
```sh
Flask Error
	If you get Error: No such command init, please create .env file
	.env will contain the following {
		FLASK_APP=vote
		FLASK_APP=api
		FLASK_ENV=development
		APP_CONFIG=api.cfg
	}
```
```sh
Port In Use Error 
	sudo lsof -i -P -n | grep LISTEN
	kill <port id>
```
## Developer Ops: </br>
```sh
For Ops role, I will be using Caddy for webserver and Gunicorn for WSGI server
	Two host open for each Microservices.

	User will be able to access to Post or Vote Microservices by using these hosts:

		localhost:2015/post
		localhost:2015/vote

	Load Balancer
		Round Robin methods have been implemented for load balancing requests
		--access-logfile - also have been implemented for testing of load balancing requests in Procfile
```
# Posting Microservices </br>
## For Posting Microservices, below is the following route to specific functions 
### To view home page for post: REQUEST GET  </br>
```sh
localhost:2015/post
```
### To view all posts: REQUEST GET  </br>
```sh
localhost:2015/post/posts/all	
```
### To view a specific post: REQUEST GET </br>
```sh
localhost:2015/post/posts/<id> </br>
example: localhost:2015/post/posts/1
```
### To delete a specific post: REQUEST GET, DELETE </br>
```sh
localhost:2015/post/posts/delete/<id> </br>
example: localhost:2015/post/posts/delete/1
```
### To create: REQUEST GET, POST</br>
```sh
json format is required, all fields are required, 
localhost:2015/post/posts
Example
    {
        "Username": "User 1",
        "PostTitle": "Post Title 1",
        // "PostDate": "01/01/2020",
        "Content": "Content 1",
        "Community": "Community 1",
        "URLResource": "www.URLResource1.com"
    }
```
### To view a specific community in posts: REQUEST GET </br>
```sh
http://localhost:5000/posts/<community name> </br>
example: localhost:2015/post/posts/Community_1
```
# Voting Microservices </br>
### View all votes: http://127.0.0.1:5000/api/v1/resources/votes/all

### View votes by vote id: http://127.0.0.1:5000/api/v1/resources/votebyid/1

### Upvote a post: http://127.0.0.1:5000/api/v1/resources/upvote </br>
    Have to input in json format.  
    Example {“postID”: 10}

### Downvote a post: http://127.0.0.1:5000/api/v1/resources/downvote </br>
    Have to input in json format.  
    Example {“postID”: 11} 

### Report the number of upvotes and downvotes for a post: </br>
    http://127.0.0.1:5000/api/v1/resources/votesbypostid/101 
     
### List the n top-scoring posts to any community: </br>
    http://127.0.0.1:5000/api/v1/resources/toppostscore/3 

### Given a list of post identifiers, return the list sorted by score: </br>
    http://127.0.0.1:5000/api/v1/resources/listsortedbyscore 
    Have to input a list: Example: [10, 13, 15] 