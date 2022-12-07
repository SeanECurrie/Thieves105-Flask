from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# create Models based off of our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    img_url = db.Column(db.String)
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    base_hp = db.Column(db.Integer)
    base_att = db.Column(db.Integer)
    base_def = db.Column(db.Integer)
    base_spec_att = db.Column(db.Integer)
    base_spec_def = db.Column(db.Integer)
    base_speed = db.Column(db.Integer)
    type = db.Column(db.String(150))


    def __init__(self, title, img_url, caption, user_id,base_hp,base_att,base_def,base_spec_att,base_spec_def,base_speed, type):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id
        self.base_hp = base_hp
        self.base_att = base_att
        self.base_def = base_def
        self.base_spec_att = base_spec_att
        self.base_spec_def = base_spec_def
        self.base_speed = base_speed
        self.type = type

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class Deck(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    pokemon = db.Column(db.JSON(), nullable=False)
    
    def __init__(self, user_id, pokemon):
        self.user_id = user_id 
        self.pokemon = pokemon
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def update_db(self):
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()