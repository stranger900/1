
import os
from flask import Flask, render_template

app = Flask(__name__)

variables = [ os.environ['TEST_ENV'], 
              os.environ['LOGIN'],
              os.environ['IMAGE_NAME'],
              os.environ['BRANCH_NAME'],
              os.environ['BUILD_NUMBER'],
              os.environ['LOGIN_DB'],
              os.environ['PASSW_DB'],
              os.environ['DB_LINC']
            ]

with open ("settings.env", "w") as file:
#     for line in variables:
#        file.write(line + "\n")
     file.write(variables[0] + "\n")
     file.write(variables[1] +'/'+variables[2] +':'+ variables[3] + '-latest\n')
     file.write(variables[4] + "\n")
     file.write('LOGIN_DB : ' + variables[5] + "\n")
     file.write('PASSW_DB : ' + variables[6] + "\n")
     file.write('DB_LINC : ' + variables[7] + "\n")

@app.route('/')
def get_variables():
    print ('Hello world!')
    with open("settings.env", "r") as file:
        info = file.readlines()

    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

