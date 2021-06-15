
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello world!')

for variable, value in os.envoron.items():
    app.config[settings.env] = value

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    
    
