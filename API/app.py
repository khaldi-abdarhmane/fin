
from __future__ import division, print_function
# coding=utf-8

import os

import numpy as np

# Keras
from tensorflow.keras.preprocessing.image import load_img,img_to_array,array_to_img

from tensorflow.keras.models import Model,load_model

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer
import mlflow
import warnings
warnings.filterwarnings('ignore')
# Define a flask app
app = Flask(__name__)
model= mlflow.keras.load_model("model_mlflow")


print(model.summary())
# model._make_predict_function()          # Necessary

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')



@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        
        f = request.files['file']

        # Save thedf file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        print(file_path.__str__())
        f.save(file_path)
        
        print("llsd")
        preds = predict_class(file_path)
        
        return preds.__str__()
    return "dfsdf"


def prepare_image_for_prediction(img_path, size = (224,224)):
    # `img` is a PIL image of size 
    img = load_img(img_path, target_size=size)
    # `array` is a float32 Numpy array of shape (224, 224, 3)
    array = img_to_array(img)
    # We add a dimension to transform our array into a "batch"
    # of size (1, 224, 224, 3)
    array = np.expand_dims(array, axis=0)
    array = array/255
    return array

def predict_class(image_path):
  image_array = prepare_image_for_prediction(image_path)
  result = model.predict(image_array)
  index_max = result.argmax(axis=1)[0]
  return index_max.__str__()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)    