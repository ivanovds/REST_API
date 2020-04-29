import requests
import random

NUMBER_OF_USERS = 3
MAX_POSTS_PER_USER = 10
MAX_LIKES_PER_USER = 10
SIGN_UP_URL = 'http://127.0.0.1:8000/api/users/'
SIGN_IN_URL = 'http://127.0.0.1:8000/api/auth/token/'
CREATE_POST_URL = 'http://127.0.0.1:8000/api/posts/'
CREATE_LIKE_URL = 'http://127.0.0.1:8000/api/likes/'




def generate_user(users_amount=NUMBER_OF_USERS, pwlen=12):
	""" Generates list of users with usernames and passwords 
	using an API from https://rapidapi.com/

	users_amount - amount of users to generate
	pwlen - length of a password.

	Returns a list of users.
	"""
	querystring  = {"count": users_amount, "pwlen": pwlen, "format":"json"}
	
	url = "https://dawn2k-random-german-profiles-and-names-generator-v1.p.rapidapi.com/"
	
	headers = {
	'x-rapidapi-host': "dawn2k-random-german-profiles-and-names-generator-v1.p.rapidapi.com",
	'x-rapidapi-key': "eb6a10647bmshcf2bcc27d833802p1bcd8cjsn2a00ea66b68f"
	}

	response = requests.request("GET", url, headers=headers, params=querystring )

	profiles = response.json()
	users = list()

	print("Please wait, users are being generated...")
	for profile in profiles:		
		users.append({
				'username': profile['username'],
				'password': profile['password'],
				'token': None,
				'content': [],
				'account_created': False,
				'posts_to_create': 0,
				'posts_created': 0,
				})

	return users


def create_account(users, url=SIGN_UP_URL):
	"""	Creates user accounts using 
	a list of {'username': username, 'password': password}.

	Returns list of users.
	"""
	print("Please wait, accounts are being created...")

	for user in users:		
		response = requests.post(
				url, 
				data={
				'username': user['username'],
				'password': user['password'],
				'confirm_password': user['password'],
				})

		if response.status_code == 201:
			user['account_created'] = True

	return users



def generate_posts_amount(users, max_posts_per_user=MAX_POSTS_PER_USER):
	"""Generates random posts_to_create for every user to create."""
	print("Please wait, random posts_to_create are being generated...")

	for user in users:
		user['posts_to_create'] = random.randint(0, max_posts_per_user)

	return users



def generate_content(users):
    """ Generates and saves content for every user. 

    Approximate generation speed: 2 records per second.
    """
    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "eb6a10647bmshcf2bcc27d833802p1bcd8cjsn2a00ea66b68f"
    }

    # content_list = list()

    print("Please wait, the content are being generated...")

    for user in users:
        posts_amount = user['posts_to_create']
        while posts_amount:
            posts_amount -= 1

            response = requests.request("GET", url, headers=headers)
            user['content'].append(response.json()['content'])
    
    return users



def get_token(users, url=SIGN_IN_URL):
	"""Updates JSON Web Tokens for every user.

	Returns a list of users with fields: 'username', 'password', 'token'.
	"""
	print("Please wait, tokens are being gotten...")

	for user in users:	
		response = requests.post(
				url, 
				data={
				'username': user['username'],
				'password': user['password'],
				})

		user['token'] = 'JWT ' + response.json()['token']

	return users



def create_post(users, url=CREATE_POST_URL):
	"""Creates posts for every user up to max_posts_per_user."""

	for user in users:
		for i in range(user['posts_to_create']):

			response = requests.post(
					url, 
					data={
					'content': user['content'][i],
					},
					headers={'Authorization': user['token']}
					)

			if response.status_code == 201:
				user['posts_created'] += 1 

	return users



# def create_like(users, url=CREATE_LIKE_URL, max_likes_per_user=MAX_LIKES_PER_USER):
# 	"""Creates likes of random posts up to max_likes_per_user."""

# 	likes_to_create = random.randint(0, max_likes_per_user)

# 	for user in users:
# 		for i in range(user['posts_to_create']):

# 			response = requests.post(url, headers={'Authorization': user['token']})	




users = generate_user()
print(users)
print("---------------------------------------------------------------------------")

print(create_account(users))
print("---------------------------------------------------------------------------")

print(generate_posts_amount(users))
print("---------------------------------------------------------------------------")

print(generate_content(users))
print("---------------------------------------------------------------------------")

print(get_token(users))
print("---------------------------------------------------------------------------")

print(create_post(users))
print("---------------------------------------------------------------------------")

# print(create_like(users))
# print("---------------------------------------------------------------------------")



for user in users:
	print(user)
	print("##################")





