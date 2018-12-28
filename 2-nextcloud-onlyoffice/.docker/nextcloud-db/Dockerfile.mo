FROM postgres:11.1
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

# Mount this volume to help loading/exporting dumps
RUN mkdir /workdir
VOLUME /workdir

# Fix permissions to match host user
RUN usermod -u ${HOST_UID:-1000} postgres && groupmod -g ${HOST_GID:-1000} postgres
