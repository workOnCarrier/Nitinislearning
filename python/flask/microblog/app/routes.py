from time import sleep

from app import app
from flask import render_template, flash, redirect, url_for

from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nitin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'beautiful day'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'starry night'
        }
    ]
    #    return render_template('index.html', title='from template', user=user)
    return render_template('index.html', title='from template', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash( message=f'login requested for user:{form.username.data},'
                       f' remember_me:{form.remember_me.data}',
               category='Info')
        sleep(3)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
