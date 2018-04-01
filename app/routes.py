from app import app
from flask import render_template, redirect, flash, url_for

from flask_login import current_user
from app.models import Post

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

@app.route("/cart")
def cart():
    # if 'email' not in session:
    #     return redirect(url_for('loginForm'))
    # loggedIn, firstName, noOfItems = getLoginDetails()
    # email = session['email']
    # with sqlite3.connect('database.db') as conn:
    #     cur = conn.cursor()
    #     cur.execute("SELECT userId FROM users WHERE email = '" + email + "'")
    #     userId = cur.fetchone()[0]
    #     cur.execute("SELECT products.productId, products.name, products.price, products.image FROM products, kart WHERE products.productId = kart.productId AND kart.userId = " + str(userId))
    #     products = cur.fetchall()
    # totalPrice = 0
    # for row in products:
    #     totalPrice += row[2]
    return render_template("cart.html", products = 'dd', totalPrice=300, loggedIn='mo', firstName='mo', noOfItems=3)

@app.route("/addToCart")
def addToCart():
    # if 'email' not in session:
    #     return redirect(url_for('loginForm'))
    # productId = int(request.args.get('productId'))
    # with sqlite3.connect('database.db') as conn:
    #     cur = conn.cursor()
    #     cur.execute("SELECT userId FROM users WHERE email = '" + session['email'] + "'")
    #     userId = cur.fetchone()[0]
    #     try:
    #         cur.execute("INSERT INTO kart (userId, productId) VALUES (?, ?)", (userId, productId))
    #         conn.commit()
    #         msg = "Added successfully"
    #     except:
    #         conn.rollback()
    #         msg = "Error occured"
    # conn.close()
    return redirect(url_for('root'))

@app.route("/removeFromCart")
def removeFromCart():
    # if 'email' not in session:
    #     return redirect(url_for('loginForm'))
    # email = session['email']
    # productId = int(request.args.get('productId'))
    # with sqlite3.connect('database.db') as conn:
    #     cur = conn.cursor()
    #     cur.execute("SELECT userId FROM users WHERE email = '" + email + "'")
    #     userId = cur.fetchone()[0]
    #     try:
    #         cur.execute("DELETE FROM kart WHERE userId = " + str(userId) + " AND productId = " + str(productId))
    #         conn.commit()
    #         msg = "removed successfully"
    #     except:
    #         conn.rollback()
    #         msg = "error occured"
    # conn.close()
    return redirect(url_for('root'))
