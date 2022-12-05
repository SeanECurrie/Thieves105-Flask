from app import app
from flask import render_template

import json
from flask_login import current_user
import requests
@app.route('/')

def home():
    instructors = [{
        'name': 'Christian',
        'age': 9000
    },
    {
        'name': 'Christopher',
        'age': 'infinity'
    }]
    return render_template('index.html', names=instructors)