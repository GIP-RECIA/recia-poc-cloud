RGPD
====

L'application du règlement européen sur la protection des données (RGPD) implique la suppression des données des 
anciens utilisateurs. Les solutions doivent donc fournir des mécanismes pour supprimer ces utilisateurs qui ne sont
plus présents dans le LDAP.

NextCloud
---------
NextCloud communique sur l'[implémentation des règles liées au RGPD](https://nextcloud.com/gdpr/) dans sa solution.

De plus, la solution propose une solution documentée pour 
[nettoyer les utilisateurs LDAP](https://docs.nextcloud.com/server/stable/admin_manual/configuration_user/user_auth_ldap_cleanup.html) 
qui ne sont plus présents dans l'annuaire LDAP.

> LDAP User Cleanup is a new feature in the `LDAP user and group backend` application. 
LDAP User Cleanup is a background process that automatically searches the Nextcloud LDAP mappings table, and verifies 
if the LDAP users are still available. Any users that are not available are marked as `deleted` in the `oc_preferences` 
database table.
Then you can run a command to display this table, displaying only the users marked as `deleted`, and then you have the 
option of removing their data from your Nextcloud data directory.

Seafile
-------

Il n'y a rien de prévu dans Seafile pour la suppression des utilisateurs absents du LDAP. Il faudra écrire un script 
pour réaliser manuellement cette suppression via l'API.
