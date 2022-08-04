import sqlite3
from contextlib import closing
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from models import create_post, get_posts


""" DATABASE = './database.db'
debug = True """

app = Flask(__name__)

CORS(app)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def connect_db():
    return sqlite3.connect('database.db')

@app.route('/', methods={'GET', 'POST'})
def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    return render_template('index.html', posts=posts)

@app.route('/delete/<int:id>', methods={'GET'})
def delete_message(id):

    db = connect_db()
    db.execute('delete from posts WHERE id = ?', [id])
    db.commit()

    posts = get_posts()

    return redirect('/')
        
if __name__ == '__main__':
    app.run(debug=True)