FROM ubuntu:16.04

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

{{#DOCKER_DEVBOX_COPY_CA_CERTIFICATES}}
COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/* \
&& update-ca-certificates

ENV NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
{{/DOCKER_DEVBOX_COPY_CA_CERTIFICATES}}

RUN \
    apt-get update && \
    apt-get install --no-install-recommends -y \
        wget mysql-client supervisor nginx crudini ffmpeg python-pip \
        python2.7 libpython2.7 python-setuptools python-imaging \
        python-ldap python-mysqldb python-pylibmc python-urllib3 && \
    pip install pillow moviepy django-pylibmc && \
    apt-get remove -y --purge --autoremove python-pip && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /etc/nginx/sites-enabled/*

ENV SEAFILE_VERSION 6.3.3
ENV SEAFILE_PATH "/opt/seafile/$SEAFILE_VERSION"

RUN \
    mkdir -p /seafile "${SEAFILE_PATH}" && \
    wget --progress=dot:mega --no-check-certificate -O /tmp/seafile-server.tar.gz \
        "https://download.seadrive.org/seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz" && \
    tar -xzf /tmp/seafile-server.tar.gz --strip-components=1 -C "${SEAFILE_PATH}" && \
    sed -ie '/^daemon/d' "${SEAFILE_PATH}/runtime/seahub.conf" && \
    # Workaround for https://github.com/benoitc/gunicorn/issues/1857
    echo "secure_scheme_headers = {'X-FORWARDED-PROTO': 'https'}">> "${SEAFILE_PATH}/runtime/seahub.conf" && \
    rm /tmp/seafile-server.tar.gz

COPY seafile/etc/ /etc/
COPY seafile/scripts/ /scripts/

RUN \
    chmod +x /scripts/*.sh && \
    mkdir -p /run/seafile && \
    ln -s /run/seafile /opt/seafile/pids && \
    ln -s "${SEAFILE_PATH}" /opt/seafile/latest && \
    ln -s /etc/nginx/sites-available/seafile.conf /etc/nginx/sites-enabled/seafile.conf && \
    ln -s /scripts/setup.sh /bin/setup && \
    mkdir -p /seafile/ccnet && \
    mkdir -p /seafile/seafile-data && \
    mkdir -p /seafile/seahub-data && \
    mkdir -p /seafile/logs && \
    mkdir -p /seafile/conf

# Patch setup-seafile-mysql.py to support existing directories on setup
# This will also generate ccnet configuration inside a tmp directory as it doesn't support generation inside existing directory
RUN sed -i -r "s/seafile_config\.validate_seafile_dir\(seafile_dir\)/seafile_dir/" ${SEAFILE_PATH}/setup-seafile-mysql.py &&\
sed -i -r "s/Utils\.error\('Ccnet config dir.*/pass/" ${SEAFILE_PATH}/setup-seafile-mysql.py &&\
sed -i -r "s/self\.ccnet_dir = os.path.join\(env_mgr\.top_dir, 'ccnet'\)/self.ccnet_dir = os.path.join(env_mgr.top_dir, 'ccnet.tmp')/" ${SEAFILE_PATH}/setup-seafile-mysql.py

RUN apt-get update -y && apt-get install -y libcap2-bin && rm -rf /var/lib/apt/lists/* \
&& setcap 'cap_net_bind_service=+ep' $(which nginx)

RUN chown -R www-data:www-data /seafile
RUN chown -R www-data:www-data /run
RUN chown www-data:www-data /opt/seafile
RUN chown -R www-data:www-data /opt/seafile/latest/runtime
RUN chown -R www-data:www-data /etc/nginx
RUN chown -R www-data:www-data /scripts
RUN chown -R www-data:www-data /var/log/nginx/
RUN chown -R www-data:www-data /var/lib/nginx/

# fixuid
ADD fixuid.tar.gz /usr/local/bin
RUN chown root:root /usr/local/bin/fixuid && \
    chmod 4755 /usr/local/bin/fixuid && \
    mkdir -p /etc/fixuid
COPY seafile/fixuid.yml /etc/fixuid/config.yml

USER www-data

WORKDIR "/seafile"
VOLUME "/seafile/ccnet" "/seafile/seafile-data" "/seafile/seahub-data" "/seafile/conf"

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

