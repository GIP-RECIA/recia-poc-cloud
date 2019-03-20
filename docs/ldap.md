LDAP
====

La solution de stockage doit être capable d'exploiter les informations du LDAP pour synchroniser les informations des 
utilisateurs et des groupes. Cette intégration se fait uniquement via les solutions de stockage, NextCloud et Seafile.

NextCloud
---------

L'intégration du LDAP dans NextCloud se fait par une application spécifique qu'il est possible d'installer et de 
configurer par l'interface graphique. L'interface graphique propose des choix automatisés, mais permet également de 
configurer manuellement ses propres filtres LDAP pour plus de contrôle.

Cette application permet de synchroniser les utilisateurs et les groupes, en affectant les groupes aux utilisateurs tel
que défini dans le LDAP. 

Il existe également un écran de configuration avancé, qui permet de choisir le champs 
"Nom d'affichage" pour l'utilisateur (`displayName` par défaut) et pour le groupe (`cn` par défaut), ainsi que les 
champs pour le Quota, l'email de l'utilisateur. Il est également possible de modifier l'association groupe-membre.

Des champs supplémentaires pourraient être ajoutés aux groupes LDAP pour proposer des libellés plus parlants que le 
`cn`.

Intégration avancé
------------------

Pour intégrer des besoins spécifiques sur la synchronisation LDAP et limiter les possibilités de partage à certains 
utilisateurs uniquement en fonction de l'utilisateur connecté (Ma propre classe par exemple, mes enseignants, 
etc ...), il sera nécessaire d'écrire du code spécifique dans une App NextCloud dédiée.

NextCloud propose une option "N'autoriser les partages qu'entre membres de mêmes groupes" (dans Administration 
/ Partage), mais cela ne semble pas suffisant pour prendre en compte tous les cas d'utilisation nécessaires.

Les sources du projet permettant d'implémenter ces spécificités sont disponibles dans le repository github, 
dossier nextcloud-apps.



Seafile
-------

L'intégration du LDAP dans Seafile se fait par fichier de configuration. Les utilisateurs sont synchronisés, mais pas 
les groupes ni les rôles, car cette fonctionnalités est disponible uniquement dans la version Pro.

Il faudra donc développer un script de synchronisation spécifique pour synchroniser les groupes LDAP au sein de Seafile.

Seafile propose cependant une [API documentée](https://manual.Seafile.com/develop/web_api_v2.1.html)