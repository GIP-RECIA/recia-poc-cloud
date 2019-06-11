Thèmes
======

NextCloud et Seafile supportent tous les deux des points d'entrée pour implémenter un thème graphique sur l'application.

Les solutions d'édition ne sont pas personnalisables.

### NextCloud

NextCloud implémente une véritable fonctionnalité de thème, qui intègre la possibilité de personnaliser

 - CSS
 - JavaScript
 - Images
 - Libellé
 - Templates HTML et PHP

Il est donc possible dans NextCloud de modifier n'importe quelle partie de l'application via le thème.

Voir [Theming Nextcloud](https://docs.nextcloud.com/server/stable/developer_manual/core/theming.html)

### Seafile

Seafile lui propose la personnalisation de certains éléments uniquement via quelques variables de configuration

- Logo
- Favicon
- CSS supplémentaire
- Page d'aide

Il n'est pas possible de modifier les templates de pages, ce qui peut limiter les possibilités de personnalisation.

Voir [Seahub customization](https://manual.Seafile.com/config/seahub_customization.html).

### Personnalisation du thème en fonction de domaine d'accès

Sur ce point, aucune solution ne couvre directement le besoin.

Il est possible de le gérer au niveau du serveur web frontal, en utilisant un module de ré-écriture d'URL 
(comme `mod_rewrite` sur Apache) ou bien en configurant des variantes de VirtualHost. 

L'idée est de rediriger les URLS d'accès au thème par défault vers des dossiers de thèmes différents en fonction du 
domaine de l'URL appelante.
