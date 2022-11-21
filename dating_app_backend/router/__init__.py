from router.login import login_blueprint
from router.user_router import user_blueprint
from router.friends_router import friends_blueprint

app_blueprint = [
    login_blueprint,
    user_blueprint,
    friends_blueprint
]
