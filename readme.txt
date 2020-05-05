Team member         CWID#                 Role
Alex Tran          91297442    		Dev (Backend for Frontend)
Tu Tran            888750130		Dev (Posting Microservices)
Joseph Hoang       889782900		Dev (Voting Microservices)


Project Overview

Dev 3: Aggregating posts and votes with a BFF
	By using BFF pattern, this microservices will be pulling data from the other services and expose it in a format of RSS that can be used directly by the frontend 
	For this project, each microservices will be given a default port to ensure that all microservices will work properly all
	Posting microservices: localhost:5000/post/posts/all 	
	Voting microservices: localhost:5100/api/v1/resources/votes/all 
	BFF microservices: localhost:5200/recent

    

Instructions to run
Install Flask 
	$ pip3 install --user Flask-API python-dotenv
Install Request 
	$ pip3 install --user requests
Install foreman & Gunicorn3
	$ sudo apt install --yes ruby-foreman
	$ sudo apt install --yes gunicorn3
Install Feed Generator
	$ sudo apt update
	$ sudo apt install --yes python3-lxml
	$ pip3 install --user feedgen

RSS feeds provided by the BFF Microservices

The 25 most recent posts to any community
	http://localhost:5200/recent
The 25 most recent posts to a particular community
	http://localhost:5200/<string>/<int> 
	http://localhost:5200/school/25 
Top 25 posts to any community, sorted by score
	http://localhost:5200/score 
The top 25 posts to a particular community, sorted by score
	http://localhost:5200/score/<string>
	http://localhost:5200/score/school
The hot 25 posts to any community, ranked using Reddit hot ranking algorithm
	http://localhost:5200/hot 



