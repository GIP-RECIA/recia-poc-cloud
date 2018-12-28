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
    0 => 'nextcloud.recia-cloud-2.test',
  ),
```

```php
  'overwrite.cli.url' => 'https://nextcloud.recia-cloud-2.test',
```

- Se connecter à [https://nextcloud.recia-cloud-2.test](https://nextcloud.recia-cloud-2.test) avec le compte `admin`/`admin`.

- Dans le menu **Applications**, ajouter l'application **ONLYOFFICE** (Catégorie *Bureautique & texte*)

- Dans le menu **Paramètres** / **Administration** / **ONLYOFFICE**, configurer l'url d'accès Document Server 
`https://onlyoffice.recia-cloud-2.test/`.

Problèmes rencontrés
====================

- [ONLYOFFICE/onlyoffice-nextcloud#17](https://github.com/ONLYOFFICE/onlyoffice-nextcloud/issues/17)

L'autorité de certification "GFI Orléans" ne semble pas reconnue par NodeJS au sein du container, malgré la présence de 
la variable `NODE_EXTRA_CA_CERTS` au sein du container. Celà ne devrait pas poser de problème avec l'utilisateur de 
certificats de production fournis par une autorité réelle.

Modifier le fichier `/etc/onlyoffice/documentserver/default.json` `rejectUnauthorized:` `false` => `true`. 


