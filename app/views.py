from flask import render_template
from app import app

@app.route('/')
@app.route('/login')
def index():
    return render_template('login.html')
