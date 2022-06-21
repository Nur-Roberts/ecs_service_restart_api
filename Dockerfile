FROM python:3.7-slim-buster

RUN mkdir /app
WORKDIR /app

ENV auth_id=""
ENV aws_region=""

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

EXPOSE 5004
CMD [ "gunicorn", "app:app", "-b", "0.0.0.0:5004", "--workers", "6" ,"--timeout", "600" ]