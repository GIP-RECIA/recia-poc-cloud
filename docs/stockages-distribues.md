Stockages distribués
====================

Nextcloud
---------

NextCloud propose une fonctionnalité 
[Stockage Externe](https://docs.nextcloud.com/server/stable/admin_manual/configuration_files/external_storage_configuration_gui.html) 
(External Storage) qui permet d'accéder et de partager des fichiers de différentes sources.

Parmis ces sources, on trouve même Nextcloud, qui permet de connecté un autre NextCloud à un NextCloud central.

Cette fonctionnalité a été mise en place sur les environnements de test et fonctionne comme attendu.

Si vous souhaitez permettre le partage sur le NextCloud externe, il faut paramétrer l'authentification sur 
"Identifiants de connexion, sauvegarder dans la base de données", et active l'option "Permettre le partage". 
L'utilisateur doit s'être connecté une premièer fois sur l'autre serveur pour que cela fonctionne.

Si vous ne souhaitez pas permettre le partage sur le NextCloud externe, il vaut mieux paramétrer l'authentification sur 
"Identifiants de connexion, sauvegardés pour la session". Ce mode ne nécessite pas que l'utilisateur se soit connecté une 
première fois directement sur le NextCloud externe.

Si certains accès sont anormalement lent, il peut-être utile de désactiver la protection bruteforce via le fichier
`config.php`.

```
`auth.bruteforce.protection.enabled' => false
```

Seafile
-------

Il n'y a pas de fonction équivalente dans Seafile.
