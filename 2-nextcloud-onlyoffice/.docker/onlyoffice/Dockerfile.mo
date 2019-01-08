FROM onlyoffice/documentserver:5.2.6.3
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

{{#DOCKER_DEVBOX_CA_CERTIFICATES}}
COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN update-ca-certificates

ENV NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt
RUN sed -i -r "s/\"rejectUnauthorized\": true/\"rejectUnauthorized\": false/g" /etc/onlyoffice/documentserver/default.json
{{/DOCKER_DEVBOX_CA_CERTIFICATES}}
