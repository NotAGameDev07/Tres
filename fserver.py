import threading
import time

from flask import Flask

app = Flask(__name__)

times = {}

times['time'] = time.time()
times['flag'] = False

def cthread():
	global times
	while not times['flag']:
		times['time'] = time.time()
	print(times['flag'])

@app.route('/')
def index():
	return '<h1>{m}</h1>'.format(m=times['time']);

@app.route('/exit')
def stop():
	global times
	times['flag'] = True
	return '<h1>STOPPED</h1>'

x = threading.Thread(target=cthread)
x.start()

y = threading.Thread(target=app.run)
y.start()