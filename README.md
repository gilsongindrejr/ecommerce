# Ecommerce

Ecommerce web site using django 3, with the cart app made using django sessions. 

# Running backend server

#### Clone this repository
```
$ git clone <https://github.com/gilsongindrejr/ecommerce.git>
```

#### Access the project folder
```
$ cd ecommerce
```

#### Activate the virtual enviroment
```
$ source venv/bin/activate
```

#### Install requirements
```
$ pip install -r requirements.txt
```

#### Migrate the database
```
$ python manage.py migrate
```

#### Run server
```
$ python manage.py runserver
```

#### The server will be initiated on port 8000 - access <http://127.0.0.1:8000> 

# Testing

The tests was made using pytest.


#### Run tests and show coverage
```
$ pytest --cov
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
