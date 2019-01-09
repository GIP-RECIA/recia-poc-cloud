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

- Se connecter à [https://seafile.recia-cloud-3.test](https://seafile.recia-cloud-3.test) avec le compte `admin@example.com`/`admin`.

- Activer Collabora en ajoutant la configuration suivante au fichier `volumes/seafile-conf/seahub_settings.py`

```python
# From 6.1.0 CE version on, Seafile support viewing/editing **doc**, **ppt**, **xls** files via LibreOffice
# Add this setting to view/edit **doc**, **ppt**, **xls** files
OFFICE_SERVER_TYPE = 'CollaboraOffice'

# Enable LibreOffice Online
ENABLE_OFFICE_WEB_APP = True

# Url of LibreOffice Online's discovery page
# The discovery page tells Seafile how to interact with LibreOffice Online when view file online
# You should change `https://collabora-online.seafile.com/hosting/discovery` to your actual LibreOffice Online server address
OFFICE_WEB_APP_BASE_URL = 'https://collabora.recia-cloud-3.test/hosting/discovery'

# Expiration of WOPI access token
# WOPI access token is a string used by Seafile to determine the file's
# identity and permissions when use LibreOffice Online view it online
# And for security reason, this token should expire after a set time period
WOPI_ACCESS_TOKEN_EXPIRATION = 30 * 60   # seconds

# List of file formats that you want to view through LibreOffice Online
# You can change this value according to your preferences
# And of course you should make sure your LibreOffice Online supports to preview
# the files with the specified extensions
OFFICE_WEB_APP_FILE_EXTENSION = ('odp', 'ods', 'odt', 'xls', 'xlsb', 'xlsm', 'xlsx','ppsx', 'ppt', 'pptm', 'pptx', 'doc', 'docm', 'docx')

# Enable edit files through LibreOffice Online
ENABLE_OFFICE_WEB_APP_EDIT = True

# types of files should be editable through LibreOffice Online
OFFICE_WEB_APP_EDIT_FILE_EXTENSION = ('odp', 'ods', 'odt', 'xls', 'xlsb', 'xlsm', 'xlsx','ppsx', 'ppt', 'pptm', 'pptx', 'doc', 'docm', 'docx')
```

Problèmes rencontrés
====================

- Images docker non officielle

Il n'y a pas d'image docker officielle fournie par le projet. Pour l'instant on utilise un fork de foxel/seafile, voir 
[foxel/seafile-docker#6](https://github.com/foxel/seafile-docker/pull/6).


