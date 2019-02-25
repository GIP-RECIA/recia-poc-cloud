# Environnements docker

## Prérequis

### docker + docker-compose

Les environnements docker nécessitent [docker](https://www.docker.com) et 
[docker-compose](https://docs.docker.com/compose/) pour s'éxecuter et doivent donc être installés au préalable.

### bash

Chaque environnement s'appuie sur un même squelette composé de scripts bash. Ces scripts bash apportent des 
facilités dans l'utilisation et le déploiement des environnements docker.

*Ces squelettes ont été générés par 
[generator-docker-devbox](https://github.com/gfi-centre-ouest/generator-docker-devbox), un générateur yeoman maintenu 
par GFI.*

### nginx-proxy

Pour fonctionner, le squelette généré nécessite l'installation du container 
[nginx-proxy](https://github.com/jwilder/nginx-proxy) qui permet d'automatiser la configuration d'un reverse proxy 
frontal en fonction des containers de chaque environnement. 

Ce proxy permet d'accéder à différentes applications via HTTP/HTTPS, en discriminant par le nom de domaine (VirtualHost).

Voici le script bash qui permet d'automatiser l'installation de nginx-proxy.

```
#!/bin/bash
NGINX_PROXY_HOME="${HOME}/.nginx-proxy"

mkdir -p "${NGINX_PROXY_HOME}/vhost.d"
mkdir -p "${NGINX_PROXY_HOME}/certs"
mkdir -p "${NGINX_PROXY_HOME}/dhparam"

docker network create nginx-proxy

docker run -d -p 80:80 -p 443:443 \
  --restart unless-stopped --net nginx-proxy --name nginx-proxy \
  -v "${NGINX_PROXY_HOME}/certs:/etc/nginx/certs" \
  -v "${NGINX_PROXY_HOME}/my_proxy.conf:/etc/nginx/conf.d/my_proxy.conf:ro" \
  -v "${NGINX_PROXY_HOME}/vhost.d:/etc/nginx/vhost.d:ro" \
  -v "${NGINX_PROXY_HOME}/dhparam:/etc/nginx/dhparam" \
  -v /var/run/docker.sock:/tmp/docker.sock:ro \
  jwilder/nginx-proxy
```

### SmartCD

Il est également conseillé d'installer [SmartCD](https://github.com/cxreg/smartcd) pour automatiser l'initialisation de
chaque environnement lors du `cd` dans le dossier. 

SmartCD  n'est pas obligatoire, mais en son absence, il faut sourcer `.bash_enter` manuellement pour activer un environnement, et sourcer 
`.bash_leave` pour le désactiver.

## Environnements de démonstration

Le projet est constitué de 4 environnements pour les plateformes de démonstration. Chaque environnement est indépendant 
et est constitué d'un dossier dans les sources du projet.

* [Nextcloud + Collabora](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/1-nextcloud-collabora)
* [Nextcloud + OnlyOffice](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/2-nextcloud-onlyoffice)
* [Seafile + Collabora](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/3-seafile-collabora)
* [Seafile + OnlyOffice](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/4-seafile-onlyoffice)

Les instructions pour initialiser et démarrer ces environnements sont disponibles dans les fichiers README.md de chaque 
dossier.

Il existe également un cinquième environnement, [recia-env](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/recia-env), 
qui contient les services utilisés pour démontrer l'intégration du système d'information de l'ENT (CAS, LDAP) dans
les différentes solutions à évaluer.


Avant d'installer ou de démarrer un environnement de démonstration, il est donc nécessaire que l'environnement
 recia-env soit installé et démarré.

Cet environnement communique avec les autres au travers du réseau docker nommé `recia-env`, à créer au préalable.

```
docker network create recia-env
```
