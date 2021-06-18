
import os
from flask import Flask, render_template

#, template_folder= '/home/ubuntu/1'
app = Flask(__name__)

variables = [os.environ['TEST_ENV'], 
             os.environ['token']]

with open ("settings.env", "w") as file:
     for line in variables:
        file.write(line + "\n")

@app.route('/')
def get_incorrect_answers():
    print ('Hello world!')
    with open("settings.env", "r") as file:
        info = file.readlines()

    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

