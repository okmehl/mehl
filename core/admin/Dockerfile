# First stage to build assets
FROM node:lts-alpine3.13 as assets

RUN apk add --no-cache python2 python3 make gcc g++

COPY package.json ./
RUN npm install

COPY ./webpack.config.js ./
COPY ./assets ./assets
RUN mkdir static \
 && ./node_modules/.bin/webpack-cli


# Actual application
FROM python:3.8-slim

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update \
 && apt-get install -y curl python3-dev default-libmysqlclient-dev build-essential libffi-dev libssl-dev cargo \
 && pip3 install --upgrade pip setuptools

COPY requirements-prod.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --from=assets static ./mailu/ui/static
COPY mailu ./mailu
COPY migrations ./migrations
COPY start.py /start.py

RUN pybabel compile -d mailu/translations

EXPOSE 80/tcp
VOLUME ["/data","/dkim"]
ENV FLASK_APP mailu

CMD /start.py

HEALTHCHECK CMD curl -f -L http://localhost/ui/login?next=ui.index || exit 1
