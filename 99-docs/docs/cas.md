Intégration CAS
===============

NextCloud
---------

NextCloud propose une application (CAS user an group backend) pour implémenter le SSO via CAS.

Cependant, il n'est plus possible d'utiliser à la fois l'authentification CAS et le plugin LDAP pour gérer les
connexions d'un même pool d'utilisateur. Il faut donc faire un choix entre les fonctionnalités apportées par le plugin 
LDAP et par le plugin CAS, ce qui pose problème. Ce plugin n'est donc finalement pas une option.

Il existe également une application officielle et plus générique: SSO & SAML authentication. Cette application à 
l'avantage d'être compatible avec le plugin LDAP.

Après avoir réalisé de nombreux tests, l'authentification SAML proposée par ce plugin est la seule option viable pour 
que l'ensemble fonctionne comme attendu. 

Les environnements docker nextcloud sont paramétrés pour utiliser ce protocole et prouvent le fonctionnement du SSO
avec CAS 6.

Le Single Sign Out a été testé et fonctionne comme attendu en SAML. Il est important de configurer la propriété 
`metadataLocation` pour que le SLS (Single Logout Service) de Nextcloud soit enregistré auprès de CAS.

```
{
  "@class": "org.apereo.cas.support.saml.services.SamlRegisteredService",
  "serviceId": "https?://nextcloud\\.pce-cloud-2\\.test/apps/user_saml/saml/metadata",
  "name": "NextCloud 2",
  "metadataLocation" : "https://nextcloud.pce-cloud-2.test/apps/user_saml/saml/metadata",
  "id": 10000002,
  "usernameAttributeProvider": {
    "@class": "org.apereo.cas.services.PrincipalAttributeRegisteredServiceUsernameProvider",
    "usernameAttribute": "uid"
  },
  "attributeReleasePolicy": {
    "@class": "org.apereo.cas.services.ReturnAllAttributeReleasePolicy"
  }
}
```

Ainsi, lorsque l'utilisateur se déconnecte du CAS, sa session Nextcloud est invalidée, et le lien "Se déconnecter" de
Nextcloud pointe vers l'url de logout du CAS.

Seafile
-------

L'intégration directe à CAS n'est pas disponible dans la version gratuite de Seafile. Il est possible de configurer
Shibboleth via Apache, donc la configuration de CAS doit pouvoir se faire par ce biais.
