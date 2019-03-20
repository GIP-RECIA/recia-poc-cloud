NextCloud + Collabora CODE
==========================

Installation
============

- Initialiser l'environnement en incluant le fichier `docker-compose.override.install.yml` pour automatiser l'installation 
de NextCloud.

```
dc -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.override.install.yml up -d
```

*Les prochains lancements pourront se faire avec `dc up -d` uniquement.*

- Configurer les noms de domaine autorisés et l'URL publique dans le fichier `volumes/nextcloud-config/config.php`

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

- Dans le menu **Paramètres** > **Administration** > **Collabora Online**, configurer l'url d'accès Collabora Online 
`https://collabora.recia-cloud-1.test`.

LDAP
====

Pour la configuration LDAP, suivre la [documentation officielle](https://docs.nextcloud.com/server/stable/admin_manual/configuration_user/user_auth_ldap.html).

- Dans le menu **Applications**, ajouter l'application **LDAP user and group backend**

- Configurer dans l'écran **Paramètres > Intégration LDAP/AD** 

- Onglet Serveur

| Propriété | Valeur |
|--------|---|
| Hôte | ldap.recia-env |
| Port | 389 |
| DN Utilisateur | cn=admin,ou=administrateurs,dc=esco-centre,dc=fr |
| Mot de passe | admin |
| DN de base | dc=esco-centre,dc=fr |

- Onglet Utilisateurs

Choisir les classes d'objets à autoriser, par exemple ENTPerson.

- Attributs de login

Choisir le ou les attributs ldap utilisés pour le login. (ENTPersonLogin)

- Groupes

Choisir les groupes à autoriser.