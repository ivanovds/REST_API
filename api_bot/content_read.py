import requests
import json

USERS_URL = 'http://127.0.0.1:8000/api/users/'
SIGN_IN_URL = 'http://127.0.0.1:8000/api/auth/token/'
REFRESH_TOKEN_URL = 'http://127.0.0.1:8000/api/auth/token/refresh/'
POSTS_URL = 'http://127.0.0.1:8000/api/posts/'
ANALYTICS_URL = 'http://127.0.0.1:8000/api/analytics/'


with open('users_file.txt', 'r') as filehandle:
	users = json.load(filehandle)


print(users)
print(type(users))
