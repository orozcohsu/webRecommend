#!/usr/bin/python python

# Author: Orozco Hsu
# Date: 2019-09-18
# Work with longdb

from flask import Flask, request, make_response, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_script import Server, Manager
from flask_moment import Moment
from datetime import datetime, timedelta
from others.flask_uuid import FlaskUUID
from random import randint

import uuid, json
import pyodbc


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
FlaskUUID(app)

expire_date = datetime.now()
expire_date = expire_date + timedelta(days=90)

@app.route('/')
def index():
    if 'id' in request.cookies:
        id = request.cookies.get('id')
        return redirect(url_for('user', id=id))
    else:
        return redirect(url_for('user', id=randint(1,5)))

@app.route('/user/<id>')
def user(id):
    resp = make_response(render_template('index.html', id=id, current_time=datetime.utcnow()))
    resp.set_cookie('id', id, expires=expire_date)
    return resp

@app.route('/product')
def product():
    if 'id' in request.cookies:
        id = request.cookies.get('id')
        return render_template('product.html', id=id)
    else:
        return redirect(url_for('index'))

@app.route('/product/<pid>/<id>')
def detail(pid,id):
    return render_template('detail.html', pid=pid, id=id)

@app.route('/recommend')
def recommend():
    if 'id' in request.cookies:
        #longdb
        cnxn = pyodbc.connect("DSN=SpliceODBC64")
        cursor = cnxn.cursor()

        id = request.cookies.get('id')

        cursor.execute("select item, score from recommend where uuid ='" + id + "';")
        result = cursor.fetchall()
        cnxn.close()

        """
        # db query or session query
        result=db.engine.execute(text('select * from iii.recommend'))
        result=session.query(queryRecommend).filter_by(uuid=id).order_by(score).limit(5).all()
        """

        return render_template('recommend_longdb.html', result=result)
    else:
        return redirect(url_for('index'))

@app.route('/writeback', methods=['POST'])
def writeback():
    if request.method == 'POST':
        id = request.form['id']
        pid = request.form['pid']
        rating = request.form['rating']

        cnxn = pyodbc.connect("DSN=SpliceODBC64")
        cursor = cnxn.cursor()

        cursor.execute("insert into weblog(uuid,item,rating) values ('" + id + "','" + pid + "','" + rating + "');")
        cnxn.commit();
        
        cnxn.close()

        return json.dumps({'status':'OK', 'id':id, 'pid':pid, 'rating':rating })

def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    manager.add_command("runserver", Server(host='0.0.0.0', port='5000', threaded=True))
    manager.run()
