Stockages distribués
====================

Nextcloud
---------

NextCloud propose une fonctionnalité 
[Stockage Externe](https://docs.nextcloud.com/server/stable/admin_manual/configuration_files/external_storage_configuration_gui.html) 
(External Storage) qui permet d'accéder et de partager des fichiers de différentes sources.

Parmis ces sources, on trouve même Nextcloud, qui permet de connecté un autre NextCloud à un NextCloud central.

Cette fonctionnalité a été mise en place sur les environnements de test et fonctionne comme attendu.

- Configurer les espaces de stockage NextCloud avec l'authentification "Identifiants de connexion, sauvegarder dans la base de données".

- Activer l'option "Permettre le partage"

- Désactiver la protection bruteforce via le fichier config.php si certains accès sont anormalement lents.

```
`auth.bruteforce.protection.enabled' => false
```

Seafile
-------

Il n'y a pas de fonction équivalente dans Seafile.
