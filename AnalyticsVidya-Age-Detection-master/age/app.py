#our web app framework!

#you could also generate a skeleton from scratch via
#http://flask-appbuilder.readthedocs.io/en/latest/installation.html

#Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the
#HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine 
#for you automatically.
#Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the
#HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine 
#for you automatically.
#requests are objects that flask handles (get set post, etc)
from flask import Flask, render_template,request
#scientific computing library for saving, reading, and resizing images
from scipy.misc import imsave, imread, imresize
#for matrix math
import numpy as np
#for importing our keras model
import keras.models
#for regular expressions, saves time dealing with string data
import re

#system level operations (like loading files)
import sys 
#for reading operating system data
import os
#requests are objects that flask handles (get set post, etc)
from flask import Flask, render_template,request
#scientific computing library for saving, reading, and resizing images
from scipy.misc import imsave, imread, imresize
#for matrix math
import numpy as np
#for importing our keras model
import keras.models
#for regular expressions, saves time dealing with string data
from keras.preprocessing import image
from keras.preprocessing.image import load_img
from sklearn.preprocessing import LabelEncoder
#system level operations (like loading files)
import sys 
#for reading operating system data
import os
import re
#tell our app where our saved model is
sys.path.append(os.path.abspath("./model"))
from load import * 
#initalize our flask app
path1="C:/siraj/images/"
app = Flask(__name__)
#global vars for easy reusability
global model, graph
#initialize these variables
model, graph = init()


@app.route('/')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	#print("@@@@@@@@ in predict @@@@@@@")
	#whenever the predict method is called, we're going
	#to input the user drawn character as an image into the model
	#perform inference, and return the classification
	#get the raw data format of the image
	imgpath = request.form.get('buttonmain')
	print("@@@@@",imgpath,"@@@@@")
	imgpath1=path1+'54.jpg'
	x=load_img(imgpath1,target_size=(64,64))
	x=np.array(image.img_to_array(x))
	lb=LabelEncoder()
	#in our computation graph
	with graph.as_default():
		#perform the prediction
		out = model.predict(x)
		answers=lb.inverse_transform(out)
		response = answers
		return response
	

if __name__ == "__main__":
	print("**Starting Server...")
	
	# Run Server
	app.run()
