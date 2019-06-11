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

Cette fonctionnalité de thème avancé nécessite la désactivation de l'application `theming` qui permet une légère 
personnalisation via des paramétrages dans l'IHM.

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

Pour Nextcloud, il n'est possible de le gérer l'activation d'un thème spécifique par VirtualHost, car le thème 
NextCloud effectif est construit par PHP qui accède directement aux fichiers sources du thème.

Il a donc été nécessaire de créer un patch afin d'ajouter le support d'un tableau associatif dans la valeur de la 
configuration système theme. Ce tableau permet d'activer un thème en fonction d'une expression régulière évaluée sur la 
valeur du header `Host`.

```
--- a/lib/private/legacy/util.php
+++ b/lib/private/legacy/util.php
@@ -1321,6 +1321,29 @@
 	 */
 	public static function getTheme() {
 		$theme = \OC::$server->getSystemConfig()->getValue("theme", '');
+		if (is_array($theme)) {
+			$host = $_SERVER['HTTP_HOST'];
+
+			$themeFound = false;
+			$themeArray = $theme;
+			foreach (array_keys($themeArray) as $key) {
+				if (array_key_exists($key, $host)) {
+					$theme = $themeArray[$key];
+					$themeFound = true;
+					break;
+				}
+			}
+
+			if (!$themeFound) {
+				foreach (array_keys($themeArray) as $key) {
+					if (preg_match($key, $host)) {
+						$theme = $themeArray[$key];
+						break;
+					}
+				}
+			}
+
+		}
 
 		if ($theme === '') {
 			if (is_dir(OC::$SERVERROOT . '/themes/default')) {
```

Ce patch permet ainsi de configurer le thème en fonction du nom de domaine d'accès dans le fichier `config.php`.

```
'theme' => ['/.*\\.1d\\..*/' => '1d', '/.*\\.2d\\..*/' => '2d'],
```