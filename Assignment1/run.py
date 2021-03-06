from  flask import Flask, render_template, request
import sqlite3

from flask.templating import render_template_string

app = Flask(__name__)
DATABASE = 'menu.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/happy')
def happy():
    # fetch data
    con = sqlite3.connect(DATABASE)
    restaurants = []
    cur = con.execute('SELECT * FROM happy')
    for row in cur:
        restaurants.append(list(row))
    con.close()
    return render_template('results.html', 
                            title='Happy', 
                            image='happy.PNG',
                            bg_color='#ffd9d9',
                            restaurants=restaurants)

@app.route('/sad')
def sad():
    #fetch data
    con = sqlite3.connect(DATABASE)
    restaurants = []
    cur = con.execute('SELECT * FROM sad')
    for row in cur:
        restaurants.append(list(row))
    con.close()
    return render_template('results.html',
                             title='Sad', 
                             image='sad.PNG',
                             bg_color='#2E71A7',
                             restaurants=restaurants)

@app.route('/cold')
def cold():
    #fetch data
    con = sqlite3.connect(DATABASE)
    restaurants = []
    cur = con.execute('SELECT * FROM cold')
    for row in cur:
        restaurants.append(list(row))
    con.close()
    return render_template('results.html',
                             title='Cold', 
                             image='cold.PNG',
                             bg_color='#d0e7f2',
                             restaurants=restaurants)

@app.route('/angry')
def angry():
    #fetch data
    con = sqlite3.connect(DATABASE)
    restaurants = []
    cur = con.execute('SELECT * FROM angry')
    for row in cur:
        restaurants.append(list(row))
    con.close()
    return render_template('results.html',
                             title='Angry', 
                             image='angry.PNG',
                             bg_color='#c7a9ab',
                             restaurants=restaurants)