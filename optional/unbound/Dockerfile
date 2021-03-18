ARG DISTRO=alpine:3.13
FROM $DISTRO

RUN apk add --no-cache unbound curl bind-tools \
  && curl -o /etc/unbound/root.hints https://www.internic.net/domain/named.cache \
  && chown root:unbound /etc/unbound \
  && chmod 775 /etc/unbound \
  && apk del --no-cache curl \
  && /usr/sbin/unbound-anchor -a /etc/unbound/trusted-key.key | true

COPY unbound.conf /unbound.conf

CMD ["/usr/sbin/unbound", "-c", "/etc/unbound/unbound.conf"]

HEALTHCHECK CMD dig @127.0.0.1 || exit 1
