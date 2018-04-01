from app import app
from app.forms import LoginForm
from flask import render_template, redirect, flash, url_for


import numpy as np
import base64

from flask import Flask, request, render_template, make_response
from sklearn.externals import joblib
from io import BytesIO
from skimage import io as skio # pip install scikit-image
from skimage.transform import resize
from app.utils import make_mnist

clf = joblib.load('app/clf.pkl')

@app.route('/recognizer', methods=['POST'])
def recognize():
    data = request.get_json(silent=True)['image']
    data = data[22:]

    img = skio.imread(BytesIO(base64.b64decode(data)))[:,:,3]

    img = make_mnist(img)
    number = clf.predict(img.reshape(1, -1))[0]
    return make_response(str(number),200)