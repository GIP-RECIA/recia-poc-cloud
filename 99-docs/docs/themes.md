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
(comme `mod_rewrite` sur Apache) et en utilisant des variantes par VirtualHost. La configuration de ré-écriture
pourra varier en fonction du VirtualHost, permettant de faire pointer le thème par défaut vers des dossiers de thèmes 
différents.


```
<VirtualHost *:80>
    ServerName 1d.recia.com

    # Nextcloud configuration
    Include nextcloud.common.conf

    # Rewrite theme to a custom one
    RewriteRule ^theme/example/(.*) /theme/1d/$1 [L]
</VirtualHost>

<VirtualHost *:80>
    ServerName 2d.recia.com

    # Nextcloud configuration
    Include nextcloud.common.conf

    # Rewrite theme to a custom one
    RewriteRule ^theme/example/(.*) /theme/2d/$1 [L]
</VirtualHost>
```

La configuration est semblable pour nginx (testé sur environnement de démo)

```
server {
    listen 80 default_server;
    server_name  _;

    include nextcloud-server.conf;
}

server {
    listen 80;
    server_name nextcloud.1d.pce-cloud-2.test;

    include nextcloud-server.conf;

    rewrite ^/themes/default/(.*)$ /themes/1d/$1;
}

server {
    listen 80;
    server_name nextcloud.2d.pce-cloud-2.test;

    include nextcloud-server.conf;
    rewrite ^/themes/default/(.*)$ /themes/2d/$1;
}
```
