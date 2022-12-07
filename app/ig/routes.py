from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import PostForm
from app.models import Post
import requests
import json

ig = Blueprint('ig', __name__, template_folder='ig_templates')






@ig.route('/posts/create', methods=["GET", "POST"])
@login_required
def create_post():
    
        form = PostForm()
        if request.method == 'POST':
            if form.validate():
                pokemon_name= form.title.data
                url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
                response = requests.get(url)
                if response.ok == True:
                    data=response.json()
                    title = data["name"]
                    img_url = data["sprites"]["other"]["dream_world"]["front_default"]
                    caption = data["abilities"][0]["ability"]["name"]
                    base_hp = data["stats"][0]["base_stat"]    
                    base_att = data["stats"][1]["base_stat"]
                    base_def= data["stats"][2]["base_stat"]
                    base_spec_att = data["stats"][3]["base_stat"]
                    base_spec_def = data["stats"][4]["base_stat"]
                    base_speed = data["stats"][5]["base_stat"]
                    type = data["types"][0]["type"]["name"]   
                    # title = form.title.data
                    # img_url = form.img_url.data
                    # caption = form.caption.data
            print(title, img_url, caption)
            post = Post(title, img_url, caption, current_user.id,base_hp,base_att,base_def,base_spec_att,base_spec_def,base_speed, type)
            post.save_to_db()
            
            return redirect(url_for('ig.view_posts'))
        return render_template('create_post.html', form=form)
   
            
@ig.route('/posts')
def view_posts():
    
    posts = Post.query.all()
    print(posts)
    return render_template('feed.html', posts = posts[::-1])

# Dynamic Routes
@ig.route('/posts/<int:post_id>')
def view_single_post(post_id):
    post = Post.query.get(post_id)
  
    return render_template('single_post.html', post=post)


@ig.route('/posts/update/<int:post_id>', methods=['GET', 'POST'])

def update_post(post_id):
    form = PostForm()
    post = Post.query.get(post_id)
    
    if request.method == 'POST':
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data

            #update post  on Attributes:
            post.title = title
            post.img_url = img_url
            post.caption = caption
            
            # update post on database

            post.update_db()
            return redirect(url_for('ig.view_posts'))
    return render_template('update_post.html', form=form, post=post)

    
@ig.route('/posts/delete/<int:post_id>')

def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        post.delete_from_db()
    
    return redirect(url_for('ig.view_posts'))