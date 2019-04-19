NextCloud + OnlyOffice
======================

Installation
============

- Initialiser l'environnement en incluant le fichier `docker-compose.override.install.yml` pour automatiser l'installation 
de NextCloud.

```
dc -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.override.install.yml up -d
```

*Les prochains lancements pourront se faire avec `dc up -d` uniquement.*

- Configurer les noms de domaine autorisés et l'URL publique dans le fichier `volumes/nextcloud-config/config.php`

```php
  'trusted_domains' => array ('nextcloud.pce-cloud-2.test'),
```

- Configurer les [trusted_proxies](https://docs.nextcloud.com/server/15/admin_manual/configuration_server/reverse_proxy_configuration.html) 
si l'application est placée derrière un load balancer ou un reverse proxy.

```php
  'trusted_proxies' => array ('172.0.0.0/8'),
```

```php
  'overwrite.cli.url' => 'https://nextcloud.pce-cloud-2.test',
```

- Se connecter à [https://nextcloud.pce-cloud-2.test](https://nextcloud.pce-cloud-2.test) avec le compte `admin`/`admin`.

- Dans le menu **Applications**, ajouter l'application **ONLYOFFICE** (Catégorie *Bureautique & texte*)

- Dans le menu **Paramètres** > **Administration** > **ONLYOFFICE**, configurer l'url d'accès Document Server 
`https://onlyoffice.pce-cloud-2.test/`. Dans les paramètres avancés, choisir Adresse du serveur pour les demandes 
internes du service d'édition de document : `https://nextcloud.pce-cloud-2.test/`.

Problèmes rencontrés
====================

- [ONLYOFFICE/onlyoffice-nextcloud#17](https://github.com/ONLYOFFICE/onlyoffice-nextcloud/issues/17)

L'autorité de certification "GFI Orléans" ne semble pas reconnue par NodeJS au sein du container, malgré la présence de 
la variable `NODE_EXTRA_CA_CERTS` au sein du container. Celà ne devrait pas poser de problème avec l'utilisation de 
certificats de production fournis par une autorité réelle.

Modifier le fichier `/etc/onlyoffice/documentserver/default.json` `rejectUnauthorized:` `false` => `true`. 

Cette modification est intégrée au Dockerfile, et ne devrait pas être utilisée en production.

- Ajout de certificats spécifiques dans NextCloud

NextCloud utilise une gestion spécifique des certificats racines, et ne prends pas en compte les certificats installés
sur le système. Cela peut poser problème lorsqu'on tente de télécharger un fichier via un Stockage Externe NextCloud, 
pour la validation du certificat SSL.

Le `occ-import-system-certs` du container Docker permet d'importer tous les certificats spécifiques du système dans 
NextCloud.

```
dc exec nextcloud occ-import-system-certs
```

- Certains patchs sont à appliquer sur les sources de NextCloud. Les patchs sont présents dans le dossier 
`.docker/nextcloud/patches` et correspondent à des Pull Requests ouverts sur le 
[github de nextcloud](https://github.com/nextcloud/docker). Ces patchs sont copiés dans le container et peuvent être 
appliqués avec la commande suivante.

```
dc exec nextcloud apply-nextcloud-patches
```

- Lors d'un scan positif a l'antivirus, le message d'erreur affiché n'est pas approprié 
(Voir [issue Github](https://github.com/nextcloud/files_antivirus/issues/119))

LDAP
====

Pour la configuration LDAP, suivre la [documentation officielle](https://docs.nextcloud.com/server/stable/admin_manual/configuration_user/user_auth_ldap.html).

- Dans le menu **Applications**, ajouter l'application **LDAP user and group backend**

- Configurer dans l'écran **Paramètres > Intégration LDAP/AD** 

- Onglet Serveur

| Propriété | Valeur |
|--------|---|
| Hôte | ldap.recia-env |
| Port | 389 |
| DN Utilisateur | cn=admin,ou=administrateurs,dc=esco-centre,dc=fr |
| Mot de passe | admin |
| DN de base | dc=esco-centre,dc=fr |

- Onglet Utilisateurs

Choisir les classes d'objets à autoriser, par exemple ENTPerson.

- Attributs de login

Choisir le ou les attributs ldap utilisés pour le login. (ENTPersonLogin)

- Groupes

Choisir les groupes à autoriser.

- Dans l'onglet Expert

Choisir au niveau de la section "Passer outre la détection des UUID", Attribut UUID pour les Utilisateurs: `uid`.

CAS
===

Prérequis: CAS doit être configuré comme 
[IdP SAML2](https://apereo.github.io/cas/6.0.x/installation/Configuring-SAML2-Authentication.html) via 
`org.apereo.cas:cas-server-support-saml-idp`.

Installer l'application "Authentification SSO & SAML".

Choisir SAML, puis configurer les valeurs suivantes

- Attribut pour relier l'IUD: `uid`
- Identifiant de l'entité IdP: `https://cas.recia-env.test/cas/idp`
- Certificat X.509 du fournisseur de service: `MIIC+zCCAeOgAwIBAgIJAMO1Gyp417waMA0GCSqGSIb3DQEBBQUAMBQxEjAQBgNVBAMMCWdmaS53b3JsZDAeFw0xOTA0MTUxNDU2MTdaFw0yOTA0MTIxNDU2MTdaMBQxEjAQBgNVBAMMCWdmaS53b3JsZDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALz2yqcL2Vh7KNYMkgUY42lnASHtnF1LtPWoWY33o/2gXOaEcOb0WbcFTe6D0P01w7XP+Ex+67+U9WSvBWkBUYJhg0RiPUcosLuf1Tlu2LN7hc+rKi2nhMzNtL9jtOKP5LoK4P+jiGLU7eyDeUF6f1JLi8YmzOM6ZwIDTm2bfwd3M7MM9HLGsUfx3N4IToWVT+fAMeQzX2MSnZlo4R1FDo8lmRsEor6O/MSGzqC9+ezfXVy/BIObkbDBsJ07OlJZ8lUC4ExdIuTcuW9LrnoVcNYdljiren8M4N0BsorQgevybcHPYPN+Df3vWtCipQMB8qyW8osZFEcms9EEJUOPABUCAwEAAaNQME4wHQYDVR0OBBYEFBBN+NkeidU0cJEJUlIHsPMD3XnCMB8GA1UdIwQYMBaAFBBN+NkeidU0cJEJUlIHsPMD3XnCMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBAC89ElsnY4WIHha2mS9NWI4syExOsjHalOEofNA1zn36aFz75DgviUlAywl/rc/Bpm0Aysca6qM8gDGjqMIuj4IotFLQbUBAkfbi/nIfcmlhnftYxa9FDeBUMvfZQ/hEOk5FOhjegGtJ+Ieq/l1quMwiEYjqaKBphW+Qx0dl12uUjFICros+2L523sSEw+9mV4Y9pMXLZsSrWl9xqEx327gXu4YIC225F5VIe7doSNWNdcko+FeFJaGk+wSK+UZm1EOhZHzTPTUEKjaBg0te035AeAHwwRPfbo3eEHvaGnGUItgZyW+bYxNl24a41G0KpNdae0S/eUCPZJpzBVy/QBg=`
- Clé privée du fournisseur de service : `MIIEpQIBAAKCAQEAvPbKpwvZWHso1gySBRjjaWcBIe2cXUu09ahZjfej/aBc5oRw 5vRZtwVN7oPQ/TXDtc/4TH7rv5T1ZK8FaQFRgmGDRGI9Ryiwu5/VOW7Ys3uFz6sq LaeEzM20v2O04o/kugrg/6OIYtTt7IN5QXp/UkuLxibM4zpnAgNObZt/B3czswz0 csaxR/Hc3ghOhZVP58Ax5DNfYxKdmWjhHUUOjyWZGwSivo78xIbOoL357N9dXL8E g5uRsMGwnTs6UlnyVQLgTF0i5Ny5b0uuehVw1h2WOKt6fwzg3QGyitCB6/Jtwc9g 834N/e9a0KKlAwHyrJbyixkURyaz0QQlQ48AFQIDAQABAoIBAQCiEAsoD0p9z0rr oWZOhtTrXhMjlRTpEvgFRDhiQMRdzn4+mdH20hRrmloHOPgxYj4SnWX3vVbVPZzk mBLMxvuwFY+uQ48Ii4ZftCn8Euw5qrPNsp/+/dAwki/1gT7unLhvMstblFZxZOsV UIDbPoMaAn7DGB3auAkGOe22pYjhzcj9GJDwj7GcHzYc9AwUZWPY6oWerXNZa6Te DrfpoqIZu3oR2Mw+bDjyKXA3o/KADL5QK0HR/FCme3i8gVGtacF5KmRLG7a/9FUN 3nX+WDZT70+7jELZLTqKDR2LdjR3c31A46q4bqtmi66pI5XR4nCM/G5/WEjUMSwp a/eS8fqBAoGBAOpGx5xrf+h5A78kZuHeybo/kCSKMfYVQpmO9AV1o7NLabTq/hmG Y6hQcRM6fzisiol0qITi1CRLMSIcxAfolVrwettaYBgZfI7oo3ZBDEJ3aDVccO98 1m+wdhE4686hp4xdBwtJBvSYuGc6WwN6xt5I+7SS3EXFWYgGYjEot1m1AoGBAM58 ZEBMZOTf40CZUKOzbXQm6bs6EFdXWr4pPQFUK2FNZEC2ciIgDPHMmgXjr94YdZeD WfKTZHd/72oGMVjLwg4Tnp37W3IjwKoLaXsRH37d/ihf9hFEVf0NqreTWBBfvYME KEBnkx/W0cnb0XZWvB5OmvLIkfVjLlB53+MMXYjhAoGBAJteO20yIc7DysdN1ek/ vhsFoouJFt8zdEqwcobYYKs8fSsdmUzGQntSddshtVOZofrM4iHW6If1Ue1klGEG T17TEzc79XSmGmQQRq/bLc06sWKKHt/Es9W4emSrkj8kGCDPZSeH09QNIGZdXhSt rQun7T3xE6I14k2CpkYh0Y7tAoGAB2hA9GmJKQi7D0MwuF6ka4lF0ziXA3sXv0Cd dqG9WKU9FnE1EPJTZI0xbUqosW/xL/k/TctpzDujrAsC1CujD3w2sXYl5qdPrwnv w8Fufs+Z4XrnyeDIsOY/nIxFmXjFxKBujTjp9zdumS4wim08HF43gsQdME9ZhvuI Q43bASECgYEAkJE7zZ2m2l9lhc1s2w3A4iImrWSV5ULlhc5A0kmV/qhLX0Fjo4H3 X/HY295wYjsIAqYnDD+9aDcIqLHUFRXwnTpvlOY9jriowGHLvSZbqZMZdMjIvOKf BvEu1FqkN16hFSjUGYgWIhtoH+Rq+QLNMd+k6SFoO5uALAsKnpc0TwQ=`
- URL cible du fournisseur d'identités à qui le fournisseur de service enverra la requête d'authentification: `https://cas.recia-env.test/cas/idp/profile/SAML2/Redirect/SSO`
- URL cible du fournisseur d'identités à qui le fournisseur de service enverra la requête de déconnexion SLO: `https://cas.recia-env.test/cas/idp/profile/SAML2/Redirect/SLO`
- Certificat public X.509 de l'IdP: `MIIDKjCCAhKgAwIBAgIVALA8F0B3qcR2Vm1vigb8NaoedklLMA0GCSqGSIb3DQEBCwUAMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVzdDAeFw0xOTA0MDUxMzE5NDRaFw0zOTA0MDUxMzE5NDRaMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKi4/m389YzAV2/KShI5Mglemy1JmBMWy+Gw0+XiU5M3jHvDo7bkRo1Ct09GhjlzLLccTZz8e86GcTvO6Z4BLlktSRpd6DJY1frGgOzxm2ATFxvbEeb9Z/VyoORxoEImChbj6ipyAeqz6ZY2tQM7CWyEqezQizLUwry1Zb7kp7ejCI1KdS1/tC6IpmTGytSUsHKxEGxLfnL90j7NXKay224d6k3ZLjXZQOekKeBLXykxZd6KMJn3GxgWJghzm55jIKYzNKvZ1XLU4V7g/2Nbj1ckxzi1cbH7qvqBCIWbw222W5u2VRYDCpa5oiBUxnsh39sl7Ez+jQUtCm3Ja2spNI0CAwEAAaNhMF8wHQYDVR0OBBYEFAC85/hvGbiOx1UGrZS0ln/O9Bj4MD4GA1UdEQQ3MDWCEmNhcy5yZWNpYS1lbnYudGVzdIYfY2FzLnJlY2lhLWVudi50ZXN0L2lkcC9tZXRhZGF0YTANBgkqhkiG9w0BAQsFAAOCAQEALQYdQmy/ovCGPmD4yxwAv/woN+buWIY/zDT7HpPKYOeT10iP24zY9eXe2AxKe2g2CcZg8pHpcSrXieRXc/ahnEE6NKbVucz8Cx7d43upPuOaSehMNeKxuzrVZ4EgbYjwBVWlO+1HCXgDsynpXggCP2Jr9Shy6foggVm8WVrY/eBTlMWMX722w5VnLaAs1bpR+yn+IxgAOhKlkBEGzjH4Yn4t6XYRsClsfa/rI8i0q0SNKHk6AZfPNaGHjbVH1DppfgjUlPEXPs2gW59iFJzD1RPiy1PjJTc+7uYison7jhGVIS8tvzbRsEGo+k8G4NcIDM1I4ySqgE/+z1hrf9O6Tg==`

(Le certificat public X.509 est a récupéré des [métadonnées SAML de l'IdP](https://cas.recia-env.test/cas/idp/metadata), sous le tag `<KeyDescriptor use="signing">...<ds:X509Certificate>`)

Les certificats et clés doivent être saisis sans espaces, sans saut de lignes et sans les entêtes `-----BEGIN ...-----` `-----END ...-----`

Si le plugin a été configuré en mode `Variable d'environnement`, il est nécessaire de modifier une valeur de 
configuration directement en base de données pour passer en mode SAML.

```
INSERT INTO appconfig (appid, configkey, configvalue) VALUES('user_saml', 'type', 'environment-variable');
UPDATE appconfig SET configvalue='saml' WHERE appid='user_saml' AND configkey='type';
```

Antivirus ClamAV
================

Pour la configuration Antivirus, activer le plugin "Antivirus for files", puis paramétrer dans "Paramètres > Sécurité"

- Mode: `Processus`
- Hôte: `clamav`
- Port: `3310`

Les fichiers seront automatiquement analysés à chaque transfert.

Environnements etablissements
=============================

- Installer le plugin External Storage sur tous les environnements.

- External storage peut causer des problèmes avec la protection bruteforce, il faut donc configurer le paramètre 
suivant dans le fichier `config.php`.

```
'auth.bruteforce.protection.enabled' => false
```


