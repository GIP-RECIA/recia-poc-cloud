FROM frolvlad/alpine-python3
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

RUN apk add --update --no-cache gcc python3-dev musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN pip install mkdocs mkdocs-material mkdocs-pdf-export-plugin
RUN apk add --update --no-cache fontconfig ttf-freefont
RUN pip install pygments
RUN apk add --update --no-cache git git-fast-import

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]

# fixuid
ADD fixuid.tar.gz /usr/local/bin
RUN chown root:root /usr/local/bin/fixuid && \
    chmod 4755 /usr/local/bin/fixuid && \
    mkdir -p /etc/fixuid
COPY mkdocs/fixuid.yml /etc/fixuid/config.yml

RUN addgroup -g 1000 mkdocs && adduser -D -u 1000 -G mkdocs mkdocs

USER mkdocs:mkdocs
