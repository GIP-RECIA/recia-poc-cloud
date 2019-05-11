FROM nginx:mainline
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

{{#DOCKER_DEVBOX_CA_CERTIFICATES}}
COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/* \
&& update-ca-certificates
{{/DOCKER_DEVBOX_CA_CERTIFICATES}}