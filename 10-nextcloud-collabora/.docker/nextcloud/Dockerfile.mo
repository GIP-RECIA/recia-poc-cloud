FROM nextcloud:14.0-apache
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

{{#DOCKER_DEVBOX_CA_CERTIFICATES}}
COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN update-ca-certificates
{{/DOCKER_DEVBOX_CA_CERTIFICATES}}

# Fix permissions to match host user
RUN usermod -u ${HOST_UID:-1000} www-data && groupmod -g ${HOST_GID:-1000} www-data
