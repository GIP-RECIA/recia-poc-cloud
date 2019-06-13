Sauvegarde
==========

La sauvegarde des données doit être mise en place au niveau de la solution de stockage. Il n'y a rien a sauvegardé sur
la solution d'édition, qui est un service sans état.

NextCloud
---------

[Backup](https://docs.nextcloud.com/server/stable/admin_manual/maintenance/backup.html)

[Restoring backup](https://docs.nextcloud.com/server/stable/admin_manual/maintenance/restore.html)

Ce processus de sauvegarde et de restauration a été validé lors d'un test sur l'environnement de démonstration.

L'inconvévient du processus de sauvegarde proposé par Nextcloud est le passage du site en mode maintenant pendant la 
réalisation du dump SQL et la création de l'archive des données.

Il est envisageable de réaliser la sauvegarde sans passage en mode maintenance. Il suffit de réaliser la sauvegarde et
la restauration normalement, mais suite à la restauration lancer la commande `occ files:scan` pour regénérer 
les métadonnées et le cache de la base de données à partir des fichiers présents. 

Ce processus peut-être très long, mais celà devrait permettre de repartir sur une base de données consistante avec le 
système de fichier. L'application reste accessible pendant le processus de scan.

A noter qu'en cas d'inconsistance entre le système de fichiers et les indexes de fichiers présents base de données
(possible avant l'execution de la commande de scan), Nextcloud peut générer des erreurs 500 pour l'utilisateur lors 
du téléchargement d'un fichier manquant, mais celà ne bloque pas l'usage du reste de l'application ni la nvagitation 
au sein des dossiers pour l'utilisateur. A l'inverse, certains fichiers déposés peuvent ne pas être visible.

Seafile
-------

[Backup and Restore from backup](https://manual.Seafile.com/maintain/backup_recovery.html)
