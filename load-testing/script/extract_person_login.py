"""
Ce script permet de générer la liste des utilisateurs à partir du fichier LDIF.
"""

import json

with open(r'C:\devel\mutagen-sessions\docker-devbox\GIP-Recia-poc-cloud\pce-env\.docker\ldap\ldif\31-people.ldif') as f:
    usernames = []
    for l in f.readlines():
        if l.startswith('ENTPersonLogin: '):
            usernames.append(l[len('ENTPersonLogin: '):].strip())
    print(json.dumps(usernames, indent=2))
