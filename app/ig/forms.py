from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
<<<<<<< HEAD
    title = StringField('title', validators=[DataRequired()])

    submit_btn = SubmitField()
=======
    title = StringField('Title', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    caption = StringField('Caption', validators=[DataRequired()])
    submit_btn = SubmitField()
>>>>>>> 3b96f0b5f4b875a16157fd8aefeff03681de30f6
