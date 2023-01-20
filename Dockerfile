FROM python:3

RUN pip install --upgrade pip

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN pip install -r requirements.txt

CMD [ "python", "/usr/src/app/index.py" ]

##ENVS##
ENV APP_NAME 'Python Flask'