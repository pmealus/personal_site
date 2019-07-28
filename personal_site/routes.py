import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from personal_site import app
from personal_site.models import Comment, Post


@app.route("/")
@app.route("/home")
def home():
    posts = Post.objects
    return render_template('home.html', posts=posts)
