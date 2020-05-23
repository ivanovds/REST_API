# Social Network REST API

REST API that allows you to interact with Social Network.
It is entirely self describing: you can find the documentation
for each API endpoint simply by visiting the URL in your browser.

## Project features
* API using JSON Web Authentication
* Model "Like" uses ContentType framework that provides generic relationships between models


## Using this API you can:
* Create account
* Create a post with text content (always made by a user)
* Like any posts
* Unlike posts, you liked before
* Get all posts or one of them
* Get all users or one of them with activity information
* Get analytics about how many likes were made
* Read API bot configuration
* Get JSON Web Token
* Refresh JSON Web Token

## Technology stack
* Django Framework 3.0.5
* Django REST Framework 3.11.0
* Django REST Framework JWT 1.11.0

## Installation

* Clone repository:
```bash
git clone https://github.com/ivanovds/REST_API
```

* Go to the project folder:
```bash
cd project-container
```

* Create environment variables file:
```bash
cp project/api/env.example project/api/.env
```

* Create a virtual environment:

On macOS and Linux:
```bash
python3 -m venv venv
```
On Windows:
```bash
py -m venv venv
```

* Switch your virtal environment in the terminal:

On macOS and Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

* Then install all packages you need.

All requirements are stored in requirements.txt.
Use the package manager [pip](https://pip.pypa.io/en/stable/) 
to install by command:

```bash
pip install -r requirements.txt
```

* Add Django Server in Run/Debug Configuration.

* Now you can run your Django Server by command:
```bash
py manage.py runserver
```
and visit http://127.0.0.1:8000/api/v1/ 


## Documentation

API root view:
![step1](static/img/readme/1.png?raw=true "Title")

Post API:
![step2](static/img/readme/2.png?raw=true "Title")

User List-Create view:
![step3](static/img/readme/3.png?raw=true "Title")

Analytics view:
![step4](static/img/readme/4.png?raw=true "Title")

Filtered analytics view:
![step4](static/img/readme/5.png?raw=true "Title")

Get Token view:
![step4](static/img/readme/6.png?raw=true "Title")

Refresh Token view:
![step4](static/img/readme/7.png?raw=true "Title")

API config view:
![step4](static/img/readme/8.png?raw=true "Title")


## Usage
To prove authentication for a protected views you can use:
* [python requests](https://requests.readthedocs.io/en/master/)
* [httpie](https://httpie.org/)
* [postman](https://www.postman.com/)

####For example:
```bash
import requests
import json

url='http://127.0.0.1:8000/api/v1/posts/' 
jwt_token = 'JWT <your token>'
response = requests.get(url, headers={'Authorization': jwt_token})
posts = response.json()['results']
print(posts)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)