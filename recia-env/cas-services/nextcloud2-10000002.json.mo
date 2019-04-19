{
  "@class": "org.apereo.cas.support.saml.services.SamlRegisteredService",
  "serviceId": "https?://nextcloud.pce-cloud-2.{{DOCKER_DEVBOX_DOMAIN}}/index.php/apps/user_saml/saml/metadata",
  "name": "NextCloud 2",
  "metadataLocation" : "https://nextcloud.pce-cloud-2.{{DOCKER_DEVBOX_DOMAIN}}/index.php/apps/user_saml/saml/metadata",
  "id": 10000002,
  "usernameAttributeProvider": {
    "@class": "org.apereo.cas.services.PrincipalAttributeRegisteredServiceUsernameProvider",
    "usernameAttribute": "uid"
  },
  "attributeReleasePolicy": {
    "@class": "org.apereo.cas.services.ReturnAllAttributeReleasePolicy"
  }
}
