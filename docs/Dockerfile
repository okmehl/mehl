FROM python:3.8-slim AS BUILDER

ARG version=master
ENV VERSION=$version

COPY requirements.txt /requirements.txt
COPY . /docs

RUN pip3 install -r /requirements.txt \
 && mkdir -p /build/$VERSION \
 && sphinx-build -W /docs /build/$VERSION


FROM nginx:mainline-alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=BUILDER /build /build

EXPOSE 80/tcp

CMD nginx -g "daemon off;"
