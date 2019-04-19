{
  "@class": "org.apereo.cas.support.saml.services.SamlRegisteredService",
  "serviceId": "https://nextcloud.*.{{DOCKER_DEVBOX_DOMAIN}}/index.php/apps/user_saml/saml/metadata",
  "name": "HTTPS (SAML)",
  "metadataLocation" : "https://nextcloud.*.{{DOCKER_DEVBOX_DOMAIN}}/index.php/apps/user_saml/saml/metadata",
  "id": 10000002,
  "usernameAttributeProvider": {
    "@class": "org.apereo.cas.services.PrincipalAttributeRegisteredServiceUsernameProvider",
    "usernameAttribute": "uid"
  },
  "attributeReleasePolicy": {
    "@class": "org.apereo.cas.services.ReturnAllAttributeReleasePolicy"
  }
}
