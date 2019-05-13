FROM openjdk:11
LABEL maintainer="Rémi Alvergnat <remi.alvergnat@gfi.fr>"

{{#DOCKER_DEVBOX_CA_CERTIFICATES}}
COPY .ca-certificates/* /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/* \
&& update-ca-certificates
COPY cas/update-ca-certificates-1.0.0-SNAPSHOT.jar /
RUN java -jar /update-ca-certificates-1.0.0-SNAPSHOT.jar -d "/usr/local/share/ca-certificates/" -g "**/*.crt"
{{/DOCKER_DEVBOX_CA_CERTIFICATES}}

RUN git clone --depth 1 --single-branch --branch 6.0 https://github.com/apereo/cas-overlay-template.git /cas-overlay \
&& mkdir -p /etc/cas

WORKDIR /cas-overlay
RUN ./gradlew --version

COPY cas/build.gradle /cas-overlay
COPY cas/gradle.properties /cas-overlay
COPY cas/gradle /cas-overlay/gradle

RUN ./gradlew clean build

COPY cas/config/* /cas-overlay/etc/cas/config/
RUN ./gradlew copyCasConfiguration

EXPOSE 8080 8443
CMD ["./gradlew", "run"]
