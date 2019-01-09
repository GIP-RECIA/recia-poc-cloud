FROM mariadb:10.2
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

# Mount this volume to help loading/exporting dumps
RUN mkdir /workdir
VOLUME /workdir
