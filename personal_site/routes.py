import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from personal_site import app
from personal_site.blog_data import blog_data


@app.route("/")
@app.route("/home")
def home():
    posts = blog_data
    return render_template('home.html', posts=posts)
