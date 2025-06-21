from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from config import Config
from models import db, Product, Category, Tag, ProductTag, ProductPhoto, Media, ProductMedia
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simple admin user class for Flask-Login
class AdminUser(UserMixin):
    id = 1
    username = Config.ADMIN_USERNAME
    password_hash = Config.ADMIN_PASSWORD_HASH

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    if user_id == '1':
        return AdminUser()
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == Config.ADMIN_USERNAME and Config.ADMIN_PASSWORD_HASH== password:
            login_user(AdminUser())
            return redirect(url_for('product_list'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def product_list():
    # TODO: Implement product listing with search/filter
    return render_template('product_list.html')

@app.route('/product/<int:product_id>')
@login_required
def product_detail(product_id):
    # TODO: Implement product detail page
    return render_template('product_detail.html')

@app.route('/media')
@login_required
def media_list():
    # TODO: Implement media listing
    return render_template('media_list.html')

# TODO: Add routes for add/edit products, media, photos, etc.

if __name__ == '__main__':
    app.run(debug=True) 
