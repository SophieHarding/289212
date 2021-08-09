from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def fetchMenu(con):
    happy = []
    free = '0'
    #cur = con.execute('SELECT burger,price FROM happy WHERE price>=' + free)
    cur = con.execute('SELECT resturant, address,price FROM happy')
    for row in cur:
        happy.append(list(row))

    sad = []
    cur = con.execute('SELECT restaurant, address,price FROM sad')
    for row in cur:
        sad.append(list(row))

    cold = []
    cur = con.execute('SELECT restaurant,address,price FROM cold')
    for row in cur:
        cold.append(list(row))

    angry = []
    cur = con.execute('SELECT restaurant,address,price FROM angry')
    for row in cur:
        angry.append(list(row))

    return {'happy':happy, 'sad':sad, 'cold':cold, 'angry':angry}

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/happy')
# def index():
#     return render_template('happy.html')

# @app.route('/sad')
# def index():
#     return render_template('sad.html')

# @app.route('/angry')
# def index():
#     return render_template('angry.html')
