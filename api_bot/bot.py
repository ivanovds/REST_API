import requests
import random
import json

CONFIG = requests.get('http://127.0.0.1:8000/api/config/').json()

NUMBER_OF_USERS = CONFIG['number_of_users']
MAX_POSTS_PER_USER = CONFIG['max_posts_per_user']
MAX_LIKES_PER_USER = CONFIG['max_likes_per_user']
USERS_URL = CONFIG['users_url']
GET_TOKEN_URL = CONFIG['get_token_url']
REFRESH_TOKEN_URL = CONFIG['refresh_token_url']
POSTS_URL = CONFIG['posts_url']
ANALYTICS_URL = CONFIG['analytics_url']



def generate_users(users_amount=NUMBER_OF_USERS, pwlen=12):
	"""Generates list of users with usernames and passwords 
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
				'likes_to_create': 0,
				'likes_created': 0,

				})

	return users


def create_accounts(users, url=USERS_URL):
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


def generate_posts_amount(users, max_posts=MAX_POSTS_PER_USER):
	"""Generates random posts_to_create for every user to create."""
	for user in users:
		user['posts_to_create'] = random.randint(1, max_posts)

	return users


def generate_likes_amount(users, max_likes=MAX_LIKES_PER_USER):
	"""Generates random likes_to_create for every user to create."""
	for user in users:
		user['likes_to_create'] = random.randint(1, max_likes)

	return users


def generate_content(users):
    """ Generates and saves content for every user. 
	
	Uses Jokes API from rapidapi.com, that is why generating may
	take a long time.
    Approximate generation speed: 2 records per second.
    """
    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "eb6a10647bmshcf2bcc27d833802p1bcd8cjsn2a00ea66b68f"
    }

    print("Please wait, the content are being generated...")

    for user in users:
        for i in range(user['posts_to_create']):

            response = requests.request("GET", url, headers=headers)
            user['content'].append(response.json()['content'])
    
    return users


def generate_simple_content(users):
	""" Generates and saves content for every user.

	Generates simple content based on username.
	Thats is why it works faster then generate_content method.
	"""
	print("Please wait, simple content are being generated...")

	for user in users:
		for i in range(user['posts_to_create']):
			content = 'Content' + ' №' + str(i) + ' of user: ' + user['username']
			user['content'].append(content)


def get_tokens(users, url=GET_TOKEN_URL):
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


def create_posts(users, url=POSTS_URL):
	"""Creates posts for every user up to max_posts_per_user."""
	print("Please wait, posts are being created...")

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


def get_last_posts(jwt_token, url=POSTS_URL):
	"""Returns last 'PAGE_SIZE' posts in the Data Base.

	PAGE_SIZE - Django REST Framework setting.
	"""
	response = requests.get(url, headers={'Authorization': jwt_token})
	posts = response.json()['results']

	return posts


def get_like_url(post_id):
	"""Returns an url of likes endpoint for current post."""
	url = 'http://127.0.0.1:8000/api/posts/' + str(post_id) + '/likes/'

	return url


def create_random_likes(users, posts):
	"""Creates likes of random posts up to max_likes."""
	print("Please wait, random likes are being created...")

	for user in users:
		for i in range(user['likes_to_create']):
			random_index = random.randint(1, (len(posts)-1))
			random_post_id = posts[random_index]['id']
			url = get_like_url(random_post_id)

			response = requests.post(url, headers={'Authorization': user['token']})

			if response.status_code == 200:
				user['likes_created'] += 1 

	return users


def get_last_users(jwt_token, url=USERS_URL):
	"""Returns last PAGE_SIZE users in the Data Base.

	PAGE_SIZE - Django REST Framework setting.
	"""
	response = requests.get(url, headers={'Authorization': jwt_token})	
	users = response.json()

	return users


def get_user_activity_by_id(jwt_token, user_id, url=USERS_URL):
	"""Returns user`s contact and activity information."""
	url = url + f'{user_id}/'
	response = requests.get(url, headers={'Authorization': jwt_token})
	user = response.json()

	return user


def get_post_by_id(jwt_token, post_id, url=POSTS_URL):
	"""Returns a post with post_id."""
	url = url + f'{post_id}/'
	response = requests.get(url, headers={'Authorization': jwt_token})
	post = response.json()

	return post


def get_last_post_fans(jwt_token, post_id, url=POSTS_URL):
	"""Returns last PAGE_SIZE fans of this post.

	PAGE_SIZE - Django REST Framework setting.
	"""
	url = url + f'{post_id}/likes/'
	response = requests.get(url, headers={'Authorization': jwt_token})
	likes = response.json()

	return likes


def get_analytics(jwt_token, date_from=None, date_to=None, url=ANALYTICS_URL):
	"""Returns analytics about how many likes was made.
	
	Date format: '2020-04-30'
	"""
	if date_from and date_to:
		url = url + f'?date_from={date_from}&date_to={date_to}'
		print(url)
	
	response = requests.get(url, headers={'Authorization': jwt_token})
	analytics = response.json()

	return analytics


def refresh_token(user, url=REFRESH_TOKEN_URL):
	"""Saves user`s new access token."""
	raw_token = user['token'].split(' ')[-1]
	response = requests.post(url, data={'token': raw_token})
	new_raw_token = response.json()['token']
	new_jwt_token = 'JWT ' + new_raw_token
	user['token'] = new_jwt_token

	return user


def like_post_by_id(jwt_token, post_id):
	"""Creates like of post with post_id."""
	url = get_like_url(post_id)
	response = requests.post(url, headers={'Authorization': jwt_token})

	return response.status_code


def unlike_post_by_id(jwt_token, post_id):
	"""Unlikes the post with post_id."""
	url = get_like_url(post_id)
	response = requests.delete(url, headers={'Authorization': jwt_token})

	return response.status_code


def main_tests():
	"""Basic tests of Social Network API.
	
	Functionality:
	● signup users (number provided in config)
	● each user creates random number of posts with any content (up to
	max_posts_per_user)
	● After creating the signup and posting activity, posts should be liked randomly, posts
	can be liked multiple times
	"""
	users = generate_users()
	print(users)
	print("---------------------------------------")

	create_accounts(users)

	generate_posts_amount(users)
	generate_likes_amount(users)

	# generate_content(users) # slow generating
	generate_simple_content(users) # fast generating

	get_tokens(users)

	create_posts(users)

	posts = get_last_posts(users[0]['token'])

	create_random_likes(users, posts)

	print("---------------------------------------")
	num = 1
	for user in users:
		print("User №", num)
		num+=1
		print(user)
		print("---------------------------------------")

	# saving created users to the file
	with open('users_file.txt', 'w') as filehandle:
		json.dump(users, filehandle)


def other_tests():
	with open('users_file.txt', 'r') as filehandle:
		users = json.load(filehandle)
	
	user = users[0]
	jwt_token = user['token']
	user_id = 11
	post_id = 1
	date_from = '2020-04-25'
	date_to = '2020-04-30'

	print("---------- List of users: ----------")
	print(get_last_users(jwt_token))

	print(f"---------- Information about user №{user_id}: ----------")
	print(get_user_activity_by_id(jwt_token, user_id))
	
	print(f"---------- Post №{post_id}: ----------")
	print(get_post_by_id(jwt_token, post_id))

	print(f"---------- Liking of post №{post_id}: ----------")
	print(like_post_by_id(jwt_token, post_id))

	print(f"---------- Post №{post_id}: ----------")
	print(get_post_by_id(jwt_token, post_id))

	print(f"---------- Likes of post №{post_id}: ----------")
	print(get_last_post_fans(jwt_token, post_id))

	print(f"---------- Unliking of post №{post_id}: ----------")
	print(unlike_post_by_id(jwt_token, post_id))

	print(f"---------- Likes of post №{post_id}: ----------")
	print(get_last_post_fans(jwt_token, post_id))

	print("---------- Analytics of likes: ----------")
	print(get_analytics(jwt_token))

	print(f"---------- Analytics from {date_from} to {date_to}: ----------")
	print(get_analytics(jwt_token, date_from, date_to))
	
	print("---------- Old access token: ----------")
	print(jwt_token)

	print("---------- New access token: ----------")
	refresh_token(user)
	new_jwt_token = user['token']
	print(new_jwt_token)

	print("---------- Checking of new access token: ----------")
	print(get_post_by_id(new_jwt_token, post_id))


main_tests()
other_tests()