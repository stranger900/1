

FROM python:3.8-alpine

WORKDIR /docker-flask-test

ADD . /docker-flask-test

#RUN pip install -r requirements.txt
RUN pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -U flask

CMD ["python","app.py"]
