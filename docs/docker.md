Docker
======

NextCloud
---------

NextCloud est officiellement compatible avec docker et fourni une image officielle efficace, ainsi que des exemples de 
configuration docker-compose.

Seafile
-------

L'intégration de Seafile dans docker n'est pas supportée par Seafile.

Une image est fournie par la communauté, mais n'est pas bien structurée et embarque l'ensemble des services au sein 
d'un même container, base de donnée comprise, ce qui est une mauvaise pratique.

Il a fallu créer une image docker spécifique pour héberger Seafile dans un environnement docker avec docker-compose.

OnlyOffice
----------

OnlyOffice propose une image docker prête a l'emploi.

Collabora
---------

Collabora propose une image docker prête à l'emploi.
