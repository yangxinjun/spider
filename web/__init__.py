# -*- coding:utf8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, disconnect
app = Flask(__name__)
socketio = SocketIO(app)
# socketio = SocketIO(app, async_mode=None) 
from web.python.home import views
from web.python.paper import views
from web.python.video import views
from web.python.news import views
from web.python.patent import views

from web.python.config import views
@app.errorhandler(404)  
def page_not_found(e):  
	return render_template('404.html'), 404 
