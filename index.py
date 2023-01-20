from flask import Flask
from app.controller.redirect import Redirect
import os

app = Flask(__name__)

@app.route("/")
def home():
    return os.getenv('APP_NAME')

@app.route("/redirect", methods=['GET'])
def redirect():
    redirect = Redirect()
    return redirect.filter()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)