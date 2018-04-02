from app import app
from flask import render_template, redirect, flash, url_for

from flask_login import current_user
from app.models import Post, Product, Kart
from app import db

@app.route("/")
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', title='The Title',user=current_user, posts=posts)

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/nums')
def nums():
    return render_template('numbersml.html')


@app.route('/store')
@app.route('/products')
def products():
    product_list = Product.query.all()
    print(product_list)
    return render_template("products.html", products=product_list)


@app.route('/product/<int:product_id>')
def product(product_id):
    product_data = Product.query.filter_by(product_id=product_id).first()
    return render_template("product.html", data=product_data, loggedIn = True, firstName = "Mo", noOfItems = 3)


@app.route("/cart")
def cart():
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    karts = Kart.query.filter_by(user_id = current_user.id).all()
    print(len(karts))

    return render_template("cart.html", products='dd', totalPrice=300, loggedIn=current_user)


@app.route("/addToCart/<int:product_id>/<string:from_page>")
def addToCart(product_id, from_page):
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    # TODO add try ...
    kart = Kart.query.filter_by(product_id=product_id).first()


    kart = Kart(user_id = current_user.id, product_id= product_id)
    db.session.add(kart)
    db.session.commit()

    return redirect(url_for('cart'))

@app.route("/removeFromCart/<int:product_id>/<string:from_page>")
def removeFromCart(product_id, from_page):
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    kart = Kart.query.filter_by(user_id = current_user.id, product_id= product_id).first()
    db.session.delete(kart)
    db.session.commit()
    return redirect(url_for('cart'))
