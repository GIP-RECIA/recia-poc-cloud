{
  "@class": "org.apereo.cas.support.saml.services.SamlRegisteredService",
  "serviceId": "https?://nextcloud(?:\\.1d|\\.2d|)\\.pce-cloud-1\\.{{DOCKER_DEVBOX_DOMAIN}}/apps/user_saml/saml/metadata",
  "name": "NextCloud 1",
  "metadataLocation": "https://nextcloud.pce-cloud-1.{{DOCKER_DEVBOX_DOMAIN}}/apps/user_saml/saml/metadata",
  "id": 10000001,
  "usernameAttributeProvider": {
    "@class": "org.apereo.cas.services.PrincipalAttributeRegisteredServiceUsernameProvider",
    "usernameAttribute": "uid"
  },
  "attributeReleasePolicy": {
    "@class": "org.apereo.cas.services.ReturnAllAttributeReleasePolicy"
  }
}
