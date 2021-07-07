
import os
from flask import Flask, render_template

app = Flask(__name__)

variables = [ os.environ['TEST_ENV'], 
              os.environ['LOGIN'],
              os.environ['IMAGE_NAME'],
              os.environ['BRANCH_NAME'],
              os.environ['BUILD_NUMBER'] ]


with open ("settings.env", "w") as file:
#     for line in variables:
#        file.write(line + "\n")
     file.write(variables[0] + "\n")
     file.write(variables[1] +'/'+variables[2] +':'+ variables[3] + '-' + variables[4] + "\n")
     file.write(variables[4] + "\n")

@app.route('/')
def get_variables():
    print ('Hello world!')
    with open("settings.env", "r") as file:
        info = file.readlines()

    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

