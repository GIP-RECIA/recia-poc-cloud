FROM nginx:mainline
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"
{{#DOCKER_DEVBOX_COPY_CA_CERTIFICATES}}

COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/* \
&& update-ca-certificates
{{/DOCKER_DEVBOX_COPY_CA_CERTIFICATES}}

RUN apt-get update -y && apt-get install -y libcap2-bin && rm -rf /var/lib/apt/lists/* \
&& setcap 'cap_net_bind_service=+ep' $(which nginx)

RUN mkdir -p /var/cache/nginx && chown -R www-data:www-data /var/cache/nginx
RUN mkdir -p /var/www/html && chown -R www-data:www-data /var/www/html
RUN chmod ugo+w /var/run

# fixuid
ADD fixuid.tar.gz /usr/local/bin
RUN chown root:root /usr/local/bin/fixuid && \
    chmod 4755 /usr/local/bin/fixuid && \
    mkdir -p /etc/fixuid
COPY nextcloud/fixuid.yml /etc/fixuid/config.yml

USER www-data:www-data
