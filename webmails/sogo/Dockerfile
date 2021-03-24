ARG DISTRO=debian:buster-slim
ARG DEBIAN_FRONTEND=noninteractive

FROM $DISTRO as builder
WORKDIR /tmp
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \ 
  gnupg python liboath-dev libldap2-dev apt-transport-https ca-certificates build-essential fakeroot devscripts cdbs libpopt-dev zlib1g-dev libexpat1-dev cmake
RUN apt-key adv --keyserver hkp://keys.gnupg.net:80 --recv-key 0x810273C4 \
  && echo "deb https://packages.inverse.ca/SOGo/nightly/5/debian buster buster" >/etc/apt/sources.list.d/sogo.list \
  && echo "deb-src https://packages.inverse.ca/SOGo/nightly/5/debian buster buster" >>/etc/apt/sources.list.d/sogo.list
RUN set -x && apt-get update && apt-get source sogo sope wbxml2
RUN cd /tmp/wbxml2-* && debuild -b -uc -us -d && dpkg -i /tmp/*.deb
RUN set -x && apt-get build-dep -y sope
RUN cd /tmp/sope-* && debuild -b -uc -us && dpkg -i /tmp/*.deb
RUN set -x && apt-get build-dep -y sogo
RUN cd /tmp/sogo-* && debuild -b -uc -us && rm /tmp/*-dbg_* /tmp/*-dev_*

FROM $DISTRO
COPY --from=builder /tmp/*.deb /tmp/
COPY boostrap.sql /bootstrap.sql
RUN set -x \
  && apt-get update && apt-get install -y --no-install-recommends \
    dirmngr cron curl \
    gnustep-base-runtime libgnustep-base1.26 libobjc4 \
    libwbxml2-0 libglib2.0-0 liblasso3 libmemcached11 liboath0 libsodium23 libzip4 gnustep-make zip \
    libmariadb3 mariadb-client libpq5 \
  && mkdir /usr/share/doc/sogo \
  && touch /usr/share/doc/sogo/empty.sh \    
  && dpkg -i /tmp/*.deb
 
USER sogo

ENTRYPOINT [ "/bootstrap.sh" ]

CMD /usr/sbin/sogod -WONoDetach YES -WOPidFile /var/run/sogo/sogo.pid -WOPort 0.0.0.0:20000

HEALTHCHECK CMD curl -k -f -L http://localhost:20000 || exit 1