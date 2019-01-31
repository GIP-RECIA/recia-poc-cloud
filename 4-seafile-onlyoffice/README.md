Seafile + Collabora CODE
==========================

Installation
============

- Démarrer l'environnement.

```
dc up -d
```

*Si le fichier `volumes/seafile-conf/seahub_settings.py` n'existe pas, la procédure 
d'installation de seafile est automatiquement déclenchée.*

- Se connecter à [https://seafile.recia-cloud-4.test](https://seafile.recia-cloud-4.test) avec le compte `admin@example.com`/`admin`.

- Activer OnlyOffice en ajoutant la configuration suivante au fichier `volumes/seafile-conf/seahub_settings.py`

```python
# Enable Only Office
ENABLE_ONLYOFFICE = True
VERIFY_ONLYOFFICE_CERTIFICATE = False
ONLYOFFICE_APIJS_URL = 'https://onlyoffice.recia-cloud-4.test/web-apps/apps/api/documents/api.js'
ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
ONLYOFFICE_EDIT_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
```

Problèmes rencontrés
====================

- Images docker non officielle

Il n'y a pas d'image docker officielle fournie par le projet. Pour l'instant on utilise un fork de foxel/seafile, voir 
[foxel/seafile-docker#6](https://github.com/foxel/seafile-docker/pull/6).

LDAP
====

Pour la configuration LDAP, suivre la [documentation officielle](https://manual.seafile.com/deploy/using_ldap.html).

- Ajouter dans le fichier `volumes/seafile-conf/ccnet.conf` la configuration LDAP

```
[LDAP]
HOST = ldap://ldap.recia-env/
BASE = ou=people,dc=esco-centre,dc=fr
USER_DN = cn=admin,ou=administrateurs,dc=esco-centre,dc=fr
PASSWORD = admin
LOGIN_ATTR = mail
FILTER = objectclass=ENTPerson
```

Limitation: Seafile can only use **email-address-format user identifiers**.