#Python image
FROM python:3

#Install Pip and upgrade version
RUN pip install --upgrade pip

#Define workdir
WORKDIR /usr/src/app

#Copy all files to workdir
ADD . /usr/src/app

#Install all requeriments from file
RUN pip install -r requirements.txt

#Run python file
CMD [ "python", "/usr/src/app/index.py" ]

#----------ENVS----------
ENV APP_NAME 'Python Flask'