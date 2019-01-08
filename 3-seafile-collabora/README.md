Seafile + Collabora CODE
==========================

Installation
============

- Démarre l'environnement, puis executer la commande afin d'installer seafile

```
dc up -d
dc exec seafile setup
```

- Configurer les noms de domaine autorisés et l'URL publique dans le fichier `volumes/nextcloud/config/config.php`

```php
  'trusted_domains' => 
  array (
    0 => 'nextcloud.recia-cloud-3.test',
  ),
```

```php
  'overwrite.cli.url' => 'https://nextcloud.recia-cloud-3.test',
```

- Se connecter à [https://nextcloud.recia-cloud-3.test](https://nextcloud.recia-cloud-3.test) avec le compte `admin`/`admin`.

- Dans le menu **Applications**, ajouter l'application **ONLYOFFICE** (Catégorie *Bureautique & texte*)

- Dans le menu **Paramètres** / **Administration** / **ONLYOFFICE**, configurer l'url d'accès Document Server 
`https://onlyoffice.recia-cloud-3.test/`.

Problèmes rencontrés
====================

- Images docker non officielle

Il n'y a pas d'image docker officielle fournie par le projet. Pour l'instant on utilise un fork de foxel/seafile, voir 
[foxel/seafile-docker#6](https://github.com/foxel/seafile-docker/pull/6).


