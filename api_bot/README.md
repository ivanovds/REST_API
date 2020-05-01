# Automated bot

Automated bot to interact with [Social Network API](https://github.com/ivanovds/REST_API/tree/master/project-container).

## Basic functionality
Bot reads the bot API configuration and create this activity:
* signup users (number provided in config)
* each user creates random number of posts with any content (up to
max_posts_per_user)
* After creating the signup and posting activity, posts should be liked randomly, posts
can be liked multiple times

Also this bot tests all existing API endpoints. 


## Requirements

```bash
pip install -r requirements.txt
```

## Usage:
```bash
python .\bot.py
```

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)