### Setup and deployment

#### Local developement server

1. Create a python3 virtual environment.
2. I have pushed requirments.txt file.
3. pip install -r reqruirements.txt
4. Go to the folder having manage.py file
5. python manage.py runserver 
6. We can access project here : http://127.0.0.1:8000/

#### Heroku Deployment - Follow commands given Below
1. Download heroku
2. heroku login
3. heroku create
4. Create a Procfile for Heroku to run Django server through gunicorn service
5. git init
6. git add .
7. git commit -m "Pushed app to Heroku"
8. git push heroku master

