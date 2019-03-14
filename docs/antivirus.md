Antivirus
=========

NextCloud
---------

NextCloud supporte officiellement une intégration de ClamAV, permettant de scanner tous les versements de fichier avant 
enregistrement.

L'intégration de ClamAV [est simple et documentée](https://docs.nextcloud.com/server/stable/admin_manual/configuration_server/antivirus_configuration.html).

Seafile
-------

L'édition Pro [propose une intégration d'Antivirus](https://www.Seafile.com/en/product/private_server/#feature-list), 
mais cette fonctionnalité n'est pas disponible dans l'édition gratuite.

De plus, Seafile explose les fichiers stockés en fragments (chunk files) ce qui rends l'intégration d'un Antivirus 
externe délicate.
