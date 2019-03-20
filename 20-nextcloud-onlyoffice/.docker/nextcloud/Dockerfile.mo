FROM nextcloud:15.0-apache
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

{{#DOCKER_DEVBOX_CA_CERTIFICATES}}
COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN update-ca-certificates
{{/DOCKER_DEVBOX_CA_CERTIFICATES}}

# occ commands should be performed with "sudo -u www-data"
RUN apt-get update && apt-get install sudo && rm -rf /var/lib/apt/lists/*

ADD nextcloud/occ-import-system-certs /usr/local/bin/occ-import-system-certs
RUN chmod +x /usr/local/bin/occ-import-system-certs

# Fix permissions to match host user
RUN usermod -u ${HOST_UID:-1000} www-data && groupmod -g ${HOST_GID:-1000} www-data
