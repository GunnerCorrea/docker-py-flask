#Flask class
from flask import Flask

#OS class
import os
import json

#App classes
from app.controller.redirect import Redirect
from app.model.article import Article

app = Flask(__name__)

@app.route("/")
def home():
    return os.getenv('APP_NAME')

@app.route("/create", methods=['GET'])
def create():
    article = Article()
    article.create_database()
    return "created"

@app.route("/create-collection", methods=['GET'])
def create_colletion():
    article = Article()
    article.create_collection()
    return "created"
    

@app.route("/redirect", methods=['GET'])
def redirect():
    redirect = Redirect()
    id = redirect.filter()

    article = Article()

    result = article.find_url_by_id(id)

    if result['url'] is None:
        redirect.redirect_home()

    return redirect.redirect_to(result['url'])


@app.route("/insert", methods=['GET'])
def insert():
    article = Article()
    article.insert_page()
    return "INSERT"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)