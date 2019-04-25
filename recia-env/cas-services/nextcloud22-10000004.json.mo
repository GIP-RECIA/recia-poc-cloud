{
  "@class": "org.apereo.cas.support.saml.services.SamlRegisteredService",
  "serviceId": "https?://nextcloud\\.pce-cloud-22\\.{{DOCKER_DEVBOX_DOMAIN}}/apps/user_saml/saml/metadata",
  "name": "NextCloud 22",
  "metadataLocation" : "https://nextcloud.pce-cloud-22.{{DOCKER_DEVBOX_DOMAIN}}/apps/user_saml/saml/metadata",
  "id": 10000004,
  "usernameAttributeProvider": {
    "@class": "org.apereo.cas.services.PrincipalAttributeRegisteredServiceUsernameProvider",
    "usernameAttribute": "uid"
  },
  "attributeReleasePolicy": {
    "@class": "org.apereo.cas.services.ReturnAllAttributeReleasePolicy"
  }
}
