from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect, jsonify

page = Flask(__name__)
page.config['MONGO_URI'] = 'mongodb://localhost:27017/local'

mongo = PyMongo(page)

@page.route('/edit')
def edit():

    return render_template('edit.html')

@page.route('/write', methods=["POST"])
def write():

    title = request.form.get('title')
    location = request.form.get('location')
    price = request.form.get('price')
    content = request.form.get('content')

    mongo.db['dangdang'].insert_one({
        "title": title,
        "location": location,
        "price": price,
        "content": content
    })
    
    return redirect('/')

@page.route('/detail')
def detail():

    details = mongo.db['dangdang'].find_one (
        {"title": request.args.get('title')}
    ) 

    return jsonify(
        {'title': details.get('title'),
         'content': details.get('content')}
    )

@page.route('/')
def list():
    productlists = mongo.db['dangdang'].find()
    
    return render_template('list.html', productlists=productlists)

   
if __name__ == '__main__':
    page.run()