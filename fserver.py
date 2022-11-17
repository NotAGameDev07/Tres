import threading
import time

from flask import Flask, jsonify, render_template

from deck import UNO
from uno import deck

g = UNO([], deck)

app = Flask(__name__)

times = {}

a = []

times['time'] = time.time()
times['flag'] = False

def cthread():
	global times
	while not times['flag']:
		times['time'] = time.time()
	print(times['flag'])

@app.route('/')
def index():
	return '<h1>STARTED</h1>';

@app.route('/json')
def jsonned():
	global a
	return jsonify({'this': a})

@app.route('/json/<val>')
def jsonner(val):
	global a
	a += [val]

@app.route('/exit')
def stop():
	global times
	times['flag'] = True
	return '<h1>STOPPED</h1>'

@app.route('/dynup')
def dynup():
	return render_template('index.html')

x = threading.Thread(target=cthread)
x.start()

y = threading.Thread(target=app.run)
y.start()