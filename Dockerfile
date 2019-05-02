# this dockerfile is used for product deployments
FROM python:3.7-alpine


COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
 
COPY . /app
WORKDIR /app
 
ENV FLASK_ENV=prod

EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "--log-level", "INFO", "main:app" ]
