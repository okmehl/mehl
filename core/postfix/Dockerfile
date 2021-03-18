ARG DISTRO=alpine:3.13
FROM $DISTRO

RUN apk add --no-cache postfix postfix-pcre cyrus-sasl-login postfix-mysql

CMD ["postfix", "start-fg"]

HEALTHCHECK --start-period=30s CMD echo QUIT|nc localhost 25|grep "220 .* ESMTP Postfix"
