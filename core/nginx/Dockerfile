ARG DISTRO=alpine:3.13

FROM debian:buster-slim as builder
WORKDIR /tmp
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y gnupg apt-transport-https ca-certificates devscripts
RUN apt-key adv --keyserver hkp://keys.gnupg.net:80 --recv-key 0x810273C4 \
  && echo "deb https://packages.inverse.ca/SOGo/nightly/5/debian buster buster" >/etc/apt/sources.list.d/sogo.list \
  && echo "deb-src https://packages.inverse.ca/SOGo/nightly/5/debian buster buster" >>/etc/apt/sources.list.d/sogo.list
RUN set -x && apt-get update && apt-get source sogo

FROM $DISTRO
RUN mkdir -p /usr/lib/GNUstep/SOGo/WebServerResources
COPY --from=builder /tmp/sogo-*/UI/WebServerResources /usr/lib/GNUstep/SOGo/WebServerResources

# python3 shared with most images
RUN apk add --no-cache \
    python3 py3-pip git bash py3-multidict \
  && pip3 install --upgrade pip

# Shared layer between nginx, dovecot, postfix, postgresql, rspamd, unbound, rainloop, roundcube
RUN pip3 install socrate==0.2.0

# Image specific layers under this line
RUN apk add --no-cache certbot nginx nginx-mod-mail openssl curl \
 && pip3 install watchdog

COPY conf /conf
COPY static /static
COPY *.py /

EXPOSE 80/tcp 443/tcp 110/tcp 143/tcp 465/tcp 587/tcp 993/tcp 995/tcp 25/tcp 10025/tcp 10143/tcp
VOLUME ["/certs"]
VOLUME ["/overrides"]

CMD /start.py

HEALTHCHECK CMD curl -k -f -L http://localhost/health || exit 1