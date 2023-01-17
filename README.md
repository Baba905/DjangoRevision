# E-commerce microservice 

E-commerce application make with Django, python framework. The main goals of this project were to revisite django and handle docker in microservice architecture.
In this first part, I made the customer management, by implementing the Customer CRUD, Product CRUD and the Order CRUD. We add a Dockerfile, to make docker container of this django app.
Then etablish a microservice architecture from Docker-compose with the image of this app, postgres image and nginx image. 
To get the prject in local follow this step:

> git clone https://github.com/Baba905/DjangoRevision.git
***
> docker-compose up
***
> docker-compose exec -T web python manage.py migrate
***
