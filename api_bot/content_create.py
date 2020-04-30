import requests
import random
import json

NUMBER_OF_USERS = 10
MAX_POSTS_PER_USER = 5
MAX_LIKES_PER_USER = 10
SIGN_UP_URL = 'http://127.0.0.1:8000/api/users/'
SIGN_IN_URL = 'http://127.0.0.1:8000/api/auth/token/'
POSTS_URL = 'http://127.0.0.1:8000/api/posts/'



def generate_user(users_amount=NUMBER_OF_USERS, pwlen=12):
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



def create_post(users, url=POSTS_URL):
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




def get_post(user, url=POSTS_URL):
	"""Returns all existing posts in the Data Base."""
	response = requests.get(url, headers={'Authorization': user['token']})
	posts = response.json()

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
			random_post_id = posts[random.randint(1, (len(posts)-1))]['id']
			url = get_like_url(random_post_id)

			response = requests.post(url, headers={'Authorization': user['token']})

			if response.status_code == 200:
				user['likes_created'] += 1 

	return users





users = generate_user()
print(users)
print("-----------------------------------------------------------------------")

create_account(users)

generate_posts_amount(users)
generate_likes_amount(users)

# generate_content(users) # slow generating
generate_simple_content(users) # fast generating

get_token(users)

create_post(users)

posts = get_post(users[0])

create_random_likes(users, posts)


print("-----------------------------------------------------------------------")
num = 1
for user in users:
	print("User №", num)
	num+=1
	print(user)
	print("-----------------------------------------------------------------------")


# saving created users to the file
with open('users_file.txt', 'w') as filehandle:
	json.dump(users, filehandle)



