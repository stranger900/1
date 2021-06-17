

FROM python:3.8-alpine

ENV LOGIN=andriy
ENV IMAGE_NAME=$IMAGE_NAME
ENV BRANCH_NAME=$BRANCH_NAME
ENV BUILD_NUMBER=$BUILD_NUMBER
ENV TEST_ENV={{ TEST_ENV }}

WORKDIR /docker-flask-test

ADD . /docker-flask-test

RUN pip install -r requirements.txt

CMD ["python","app.py"]
