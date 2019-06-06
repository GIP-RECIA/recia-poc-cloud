FROM nextcloud:15.0.8-fpm
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"
{{#DOCKER_DEVBOX_COPY_CA_CERTIFICATES}}

COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN update-ca-certificates
{{/DOCKER_DEVBOX_COPY_CA_CERTIFICATES}}

# occ commands should be performed with "sudo -u www-data"
RUN apt-get update && apt-get install sudo && rm -rf /var/lib/apt/lists/*

# Add xdebug to remote debug custom apps
RUN yes | pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini

ADD nextcloud-php/occ-import-system-certs /usr/local/bin/occ-import-system-certs
RUN chmod +x /usr/local/bin/occ-import-system-certs

ADD nextcloud-php/apply-nextcloud-patches /usr/local/bin/apply-nextcloud-patches
RUN chmod +x /usr/local/bin/apply-nextcloud-patches

RUN mkdir -p /var/www/html && chown -R www-data:www-data /var/www/html
RUN mkdir -p /config && chown -R www-data:www-data /config
RUN mkdir -p /patches && chown -R www-data:www-data /patches

# fixuid
ADD fixuid.tar.gz /usr/local/bin
RUN chown root:root /usr/local/bin/fixuid && \
    chmod 4755 /usr/local/bin/fixuid && \
    mkdir -p /etc/fixuid
COPY nextcloud-php/fixuid.yml /etc/fixuid/config.yml

USER www-data:www-data
