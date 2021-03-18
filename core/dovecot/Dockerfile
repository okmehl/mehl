ARG DISTRO=alpine:3.13
FROM $DISTRO

RUN apk add --no-cache dovecot dovecot-lmtpd dovecot-pop3d dovecot-submissiond dovecot-pigeonhole-plugin dovecot-mysql dovecot-fts-solr rspamd-client \
  && mkdir /var/lib/dovecot

CMD ["/usr/sbin/dovecot", "-c", "/etc/dovecot/dovecot.conf", "-F"]

HEALTHCHECK --start-period=30s CMD echo QUIT|nc localhost 110|grep "Dovecot ready."
