from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required, logout_user, current_user, login_user
from .forms import SignupForm, LoginForm, ResetForm
from .models import User

auth=Blueprint('auth',__name__)


@auth.route('/register/', methods=["GET", "POST"])
def register():
    """User sign-up form for account creation."""
    form = SignupForm()
    if form.validate_on_submit():
        existing_user=User.objects(email=form.email.data).first()
        if existing_user is None:
            user = User(
                email=form.email.data,
            )
            user.set_password(form.password.data)
            user.save()
            login_user(existing_user)
            return redirect(url_for('auth.login'))
        flash('User already exist')
    return render_template(
        "register.html",
        form=form
    )

@auth.route('/login/', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('auth.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        flash('Invalid username or password cobmination')
        return redirect(url_for('auth.login'))
    return render_template(
        "login.html",
        form=form
    )

@auth.route('/reset/', methods=["GET", "POST"])
def reset():
    form = ResetForm()
    if form.validate_on_submit():
        flash('Check your mail')
    return render_template('forgotpassword.html',form=form)

@auth.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@auth.route('/settings/')
@login_required
def settings():
    return render_template('settings.html',name=current_user.email)

@auth.route('/admin/')
@login_required
def admin():
    return render_template('administration.html')

@auth.route('/contest/create/')
def create():
    return render_template('createcontest.html')

@auth.route('/contest/edit/')
def edit():
    return render_template('editcontest.html')

@auth.route('/logout/', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
