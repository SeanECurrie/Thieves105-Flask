from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, User
from .auth.routes import auth
from .ig.routes import ig
<<<<<<< HEAD
from flask_login import LoginManager
=======
from .api.routes import api
from flask_login import LoginManager
from flask_moment import Moment

>>>>>>> 3b96f0b5f4b875a16157fd8aefeff03681de30f6
app = Flask(__name__)

app.config.from_object(Config)
moment = Moment(app)
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# register blueprints
app.register_blueprint(auth)
app.register_blueprint(ig)
<<<<<<< HEAD

=======
app.register_blueprint(api)
>>>>>>> 3b96f0b5f4b875a16157fd8aefeff03681de30f6

#initialize our database to work with our app
db.init_app(app)
migrate = Migrate(app, db)
login_manager.init_app(app)
<<<<<<< HEAD
login_manager.login_view= 'auth.login'
=======
login_manager.login_view = 'auth.login'
>>>>>>> 3b96f0b5f4b875a16157fd8aefeff03681de30f6

from . import routes
from . import models