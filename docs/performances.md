Performances
============

Solution de stockage
--------------------

### Algorithmes de synchronisation

La synchronisation des fichiers proposée par Seafile est plus rapide que celle de NextCloud. Seafile explose les 
fichiers stockés en fragments (chunk files), comme git, et implémente un algorithme optimisé pour la synchronisation, 
comme rsync.

Ces choix permettent d'améliorer d'améliorer la vitesse de synchronisation.

- [NextCloud](https://github.com/nextcloud/desktop/blob/master/doc/dev/sync-algorithm.md)

- [Seafile](https://manual.Seafile.com/develop/sync_algorithm.html)

### Protocole de synchronisation

Seafile utilise par défaut un protocole non standardisé pour la synchronisation, ce qui le rends incompatible avec de 
nombreux clients de synchronisation de fichier génériques. Il existe cependant un plugin WebDav, mais on perds alors
l'avantage des performances apportées par le protocole par défaut.

NextCloud utilise WebDav pour la synchronisation des fichiers ce qui le rends plus ouvert.

### Tests de performance

***TODO***

Solution d'édition
------------------

### Architecture

Collabora est une représentation visuelle de LibreOffice hébergé sur un serveur et envoyée au navigateur. Seuls les 
éléments de contrôles et quelques fonctionnalités sont adaptés par rapport à la version Desktop de LibreOffice.

OnlyOffice lui fonctionne comme une application HTML5/JS classique, et travaille en échangeant des données en 
permanence avec le serveur. Cette architecture décharge énormément de travail du serveur vers le client.

D'après son auteur, OnlyOffice peut supporter sur un serveur double cœur jusqu’à 150 utilisateurs, tandis qu’avec 
Collabora il peut en accueillir dix seulement.

### Tests de performance

***TODO***