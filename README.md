# Pycommerce

Ecommerce web site using django 3, with the cart app made using django sessions. 

# Running the project

#### Clone this repository
```
$ git clone <https://github.com/gilsongindrejr/ecommerce.git>
```

#### Access the project folder
```
$ cd ecommerce
```

#### Build the container
```
$ docker-compose up --build -d
```

#### Migrate the database
```
$ docker-compose exec web python manage.py migrate
```
#### Create super user
```
$ docker-compose exec web python manage.py createsuperuser
```

##### The server will be initiated on port 80 - access <http://127.0.0.1> 

# Server shell
```
$ docker-compose exec web bash
```

# Testing

The tests was made using pytest.


#### Run tests and show coverage
```
$ docker-compose exec web pytest --cov
```

#### Run tests and create coverage html page
```
$ pytest --cov --cov-report=html
```

Access htmlcov folder
```
$ cd htmlcov/
```

Run python http server
```
$ python -m http.server
```

Access the server on <http://127.0.0.1:8000> 
