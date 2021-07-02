FROM python:3.8-alpine

WORKDIR /docker-flask-test

ADD . /docker-flask-test

RUN pip install -U Flask --proxy=8.8.8.8
#RUN pip install -r requirements.txt

CMD ["python","app.py"]
