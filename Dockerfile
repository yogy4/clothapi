FROM python:3.8.0-alpine

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt
COPY . /usr/src/app/
EXPOSE 5000
RUN ls -la /usr/src/app/
#USER root
RUN ["chmod", "+x", "/usr/src/app/docker-entrypoint.sh"]
# RUN python manage.py runserver
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
