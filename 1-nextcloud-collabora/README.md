NextCloud + Collabora CODE
==========================

Installation
============

- Initialiser l'environnement en incluant le fichier `docker-compose.override.install.yml` pour automatiser l'installation 
de NextCloud.

```
dc -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.override.install.yml up -d
```

- Configurer les noms de domaine autorisés et l'URL publique dans le fichier `volumes/nextcloud/config/config.php`

```php
  'trusted_domains' => 
  array (
    0 => 'nextcloud.recia-cloud-1.test',
  ),
```

```php
  'overwrite.cli.url' => 'https://nextcloud.recia-cloud-1.test',
```

- Se connecter à [https://nextcloud.recia-cloud-1.test](https://nextcloud.recia-cloud-1.test) avec le compte `admin`/`admin`.

- Dans le menu **Applications**, ajouter l'application **Collabora Online** (Catégorie *Bureautique & texte*)

- Dans le menu **Paramètres** / **Administration** / **Collabora Online**, configurer l'url d'accès Collabora Online 
`https://collabora.recia-cloud-1.test`.
