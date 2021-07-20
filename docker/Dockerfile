FROM python:3.8-alpine

WORKDIR /docker-flask-test

ADD . /docker-flask-test

RUN pip install -U Flask
#RUN pip install -r requirements.txt

CMD ["python","app.py"]
