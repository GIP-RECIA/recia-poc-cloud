Extensions
==========

Les possibilités d'extension des solutions de stockage sont a évaluer avec précision, car la solution de stockage 
choisie doit s'intégrer parfaitement à l'environnement actuel de l'ENT.

Il est préférable de limiter au maximum les modifications dans le code source même de l'application, pour être en 
mesure de mettre à jour la solution à l'avenir, en respectant si possible la procédure standard de migration.

NextCloud
---------

NextCloud propose de grandes possibilités de personnalisation et d'enrichissement spécifiques au travers des Apps. 
Ces possibilités sont très clairement documentées dans la page 
[Nextcloud developer documentation](https://docs.nextcloud.com/server/13/developer_manual/). NextCloud adopte le 
modèle MVC, et l'application est bien structurée pour permettre les extensions.

Outre la création d'Apps spécifiques, il est également possible de modifier le comportement existant au travers de 
Middleware qui permet de modifier les réponses de n'importe quel contrôleur. 

Ainsi il est possible d'intégrer des composants supplémentaires, dans n'importe quelle page.

Le theming permet également de surcharger n'importe quel fichier PHP, ce qui est également un moyen 
d'apporter une modification sans directement modifier le code source. Cette solution reste cependant a éviter, car
elle rends la mise à jour de NextCloud délicate (merge à réaliser).

L'environnement de démonstration Nextcloud intègre une App spécifique nommé `reciacustom` dans le sous-module git 
[nextcloud-custom-apps/nextcloud-recia-custom](https://github.com/GIP-RECIA/nextcloud-recia-custom). Cette application 
démontre les possibilités de personnalisations sur les facilités de collaborateurs et de partage (filtrage des 
utilisateurs par établissement). 

Seafile
-------

Seafile ne propose pas de possibilités particulières à la modification des comportements et des affichages par 
défaut.

Il est nécessaire de créer un fork pour intégrer des besoins spécifiques. Comme il est écrit en Python, il est 
certainement possible de réaliser des MonkeyPatch pour éviter la création d'un fork, mais cette pratique est risquée, 
et le manque de documentation sur le fonctionnement interne de Seafile est un problème.
