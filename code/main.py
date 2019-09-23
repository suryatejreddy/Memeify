from flask import Flask, jsonify, request
from flask.templating import render_template

import pickle
import random
import os


def get_caption(category):
	"<REDACTED>"

def get_category(category):
	"<REDACTED>"

app = Flask(__name__)

@app.route('/gsg')
def home():
	return "Welcome"

@app.route('/')
def generate():
	return render_template("generate.html")

@app.route('/find')
def hello():
	return render_template("find.html")

@app.route('/getRandomImage')
def getRandomImage():
	category = request.args.get('category')
	data = {}
	data["image_path"] = "/static/images/" + category
	random_caption = get_caption(category)
	data["upperText"] = random_caption[0]
	data["lowerText"] = random_caption[1]
	return jsonify(data)

@app.route('/getCustomImage', methods = ["GET","POST"])
def getCustomImage():    
	image = request.files.get('im_upload')

	path_to_image = '/Users/reddy/Documents/AcadStuff/sem7/ir/demo/website/static/custom/' + image.filename 
	image.save(path_to_image)

	data = {}
	data["image_path"] = "/static/custom/" + image.filename

	category = get_category(data["image_path"])
	random_caption = get_caption(category)
	
	data["upperText"] = random_caption[0]
	data["lowerText"] = random_caption[1]
	return jsonify(data)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug = True)