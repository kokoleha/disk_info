FROM python:latest

ADD . /code

WORKDIR /code

RUN apt-get update && apt-get install python3-pip -y

RUN pip3 install psutil

CMD ["python3", "./diskinfo.py"]
