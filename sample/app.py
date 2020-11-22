#Import dependencies
from flask import Flask

#Creating New Flask App Instance
app = Flask(__name__)

#Creating Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

#if __name__ == "__main__":
    #app.run(debug=True)