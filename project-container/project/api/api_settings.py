import environ
from environ import Path
root = Path('/')

env = environ.Env(
    NUMBER_OF_USERS=(int, 0),
    MAX_POSTS_PER_USER=(int, 0),
    MAX_LIKES_PER_USER=(int, 0),
    USERS_URL=(str, 'http://127.0.0.1:8000/api/v1/users/'),
    POSTS_URL=(str, 'http://127.0.0.1:8000/api/v1/posts/'),
    GET_TOKEN_URL=(str, 'http://127.0.0.1:8000/api/v1/auth/token/'),
    REFRESH_TOKEN_URL=(str, 'http://127.0.0.1:8000/api/v1/auth/token/refresh/'),
    ANALYTICS_URL=(str, 'http://127.0.0.1:8000/api/v1/analytics/'),

)

environ.Env.read_env()

