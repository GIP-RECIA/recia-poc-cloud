Intégration CAS
===============

NextCloud
---------

NextCloud propose une application (CAS user an group backend) pour intégrer le SSO fourni par CAS.

Cependant, il n'est plus possible d'utilisation à la fois l'authentification CAS et le plugin LDAP pour gérer les
connexions d'un même pool d'utilisateur. Il faut donc faire un choix entre les fonctionnalités apportées par le plugin 
LDAP et par le plugin CAS, ce qui pose problème.

Il existe également une application officielle et plus générique (SSO & SAML authentication). Cette application à 
l'avantage d'être compatible avec le plugin LDAP, et peut se paramétrer pour authentifier l'utilisateur via un Header 
HTTP ajouté par exemple via le module Apache [mod_auth_cas](https://github.com/apereo/mod_auth_cas). Il semble donc
préférable d'utilise ce plugin pour implémenter le SSO, plutôt que le plugin dédié pour CAS.

Seafile
-------

L'intégration directe à CAS n'est pas disponible dans la version gratuite de Seafile. Il est possible de configurer
Shibboleth via Apache, donc la configuration de CAS doit pouvoir se faire par ce biais.
