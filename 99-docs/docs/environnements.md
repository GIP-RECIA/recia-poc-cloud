# Environnements

## Prérequis

### docker-devbox

Les environnements docker nécessitent un environnement 
[docker-devbox](https://github.com/gfi-centre-ouest/docker-devbox) pour s'éxecuter. (Prévoir une VM dédiée)

!!! note "GFI contribue à l'OpenSource"
    docker-devbox est un composant opensource développé par GFI Informatique qui permet d'industrialiser les 
    environnements applicatifs avec Docker de docker-compose.
    [generator-docker-devbox](https://github.com/gfi-centre-ouest/generator-docker-devbox), un générateur yeoman 
    opensource créé et maintenu par GFI.
    
[docker-devbox](https://github.com/gfi-centre-ouest/docker-devbox) s'appuie sur les technologies suivantes pour
faciliter la mise en oeuvre d'environnements sous Docker: 

- Docker
- Docker-Compose
- Traefik
- SmartCD
- bash

## Environnements de démonstration

Le projet est constitué de 4 environnements pour les plateformes de démonstration. Chaque environnement est indépendant 
et est constitué d'un dossier dans les sources du projet.

* [Nextcloud + Collabora](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/1-nextcloud-collabora)
* [Nextcloud + OnlyOffice](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/2-nextcloud-onlyoffice)
* [Seafile + Collabora](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/3-Seafile-collabora)
* [Seafile + OnlyOffice](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/4-Seafile-onlyoffice)

Les instructions pour initialiser et démarrer ces environnements sont disponibles dans les fichiers README.md de chaque 
dossier.

Il existe également un cinquième environnement, [pce-env](https://github.com/GIP-RECIA/recia-poc-cloud/tree/master/pce-env), 
qui contient les services utilisés pour démontrer l'intégration du système d'information de l'ENT (CAS, LDAP) dans
les différentes solutions à évaluer.

Avant d'installer ou de démarrer un environnement de démonstration, il est donc nécessaire que l'environnement
 pce-env soit installé et démarré.

Cet environnement communique avec les autres au travers du réseau docker nommé `pce-env`, à créer au préalable.

```bash
docker network create pce-env
```
