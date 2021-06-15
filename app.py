
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello world!')

@app.route('/')
def image_name():
    with open("settings.env", "r") as f:
        for line in f:
            return(line)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    
    
