Licenses
========

Seafile
-------

Seafile est constitué de plusieurs composants distribués sous différentes license

- SeaHub: Apache 2.0
- CCNet Server: AGPLv3
- Seafile Server: AGPLv3
- Seafile: GPLv2

Les modifications apportées à Seafile Server et Seafile doivent être publiées sous une license compatible GPL.

### Seafile Pro

Seafile est porté par une société qui commercialise une édition Pro. L'édition community, gratuite et libre, doit donc 
être vue comme une version d'évaluation qui intègre les fonctionnalités essentielles uniquement.

Par exemple, la version Pro inclu un script de synchronisation des utilisateurs et groupes du LDAP vers Seafile, alors 
qu'il faudra le développer manuellement sur la version community. Idem pour l'intégration d'un antivirus.

|Number of users|Price /Year (USD/EUR)|Price for Educational /Year (USD/EUR)|
|--- |--- |--- |
|3 users|Free|Free|
|9 users|$100 in Total|$100 in Total|
|From 10 to 249|$48 /User (€44)|$24 /User (€22)|
|From 250 to 499|$44 /User (€40)|$22 /User (€20)|
|From 500 to 749|$40 /User (€35)|$18 /User (€16)|
|From 750 to 999|$35 /User (€30)|$16 /User (€14)|
|1000+|Contact us|Contact us|

[Plus de détails sur la version Pro](https://www.Seafile.com/en/product/private_server/)

!!! warning "Budget"
    Compte tenu du budget nécessaire pour le nombre d'utilisateur prévus, les fonctionnalités offertes par la version
    Pro sont écartées de l'analyse comparative des solutions.

NextCloud
---------

NextCloud est fourni sous license AGPLv3. 

Il est clairement stipulé dans la documentation de NextCloud que toutes les applications développées pour NextCloud 
doivent être publiées sous license AGPLv3 ou une autre license compatible, ce qui interdit le développement de modules 
spécifiques privés.

Collabora CODE
--------------

Collabora CODE est fourni sous license Mozilla Public License v2.0

Les fichiers modifiés sous license MPL doivent être publiés sous la même license, mais il est possible d'intégrer 
d'autres sources au sein de l'application sans avoir à la publier.

OnlyOffice
----------

OnlyOffice est fourni sous license AGPL v3

Les modifications apportées à OnlyOffice doivent être publiées sous une license compatible GPL.

La version gratuite est cependant limitée à 20 utilisateurs simultanés par serveur, et cette limite a été atteinte lors
de l'execution du test de performance. 

Il est peut-être possible d'utiliser un load balancer pour obtenir un nombre d'utilisateur simultané plus important (à Valider).

Rappels sur les licenses rencontrées
====================================

GPL (General Public License)
----------------------------

L'objectif de la licence GNU GPL, selon ses créateurs est de garantir à l'utilisateur les droits suivants (appelés 
libertés) sur un programme informatique :

  1. La liberté d'exécuter le logiciel, pour n'importe quel usage
  2. La liberté d'étudier le fonctionnement d'un programme et de l'adapter à ses besoins, ce qui passe par l'accès aux 
codes sources
  3. La liberté de redistribuer des copies
  4. L'obligation de faire bénéficier la communauté des versions modifiées. Pour la première liberté, cela exclut donc 
toutes limitations d'utilisation d'un programme par rapport à l'architecture (notamment le processeur et le système 
d'exploitation) ou à l'utilisation qui va en être faite.

La quatrième liberté passe par un choix : la deuxième autorisant de modifier un programme, il n'est pas tenu de publier
une version modifiée tant qu'elle est pour un usage personnel ; par contre, en cas de distribution d'une version 
modifiée, la quatrième liberté amène l'obligation à ce que les modifications soient retournées à la communauté sous la 
même licence.

A noter qu'il existe quelques variants de cette license

- AGPL (Affero General Public License): Lorsqu'un programme s'execute sur un serveur, le code source des modifications 
doit être disponible en téléchargement.


Apache License
--------------

Les caractéristiques majeures de la licence Apache sont, d'une part, d'autoriser la modification et la distribution du 
code sous toute forme (libre ou propriétaire, gratuit ou commercial) et, d'autre part, d'obliger le maintien du 
copyright lors de toute modification (et également du texte de la licence elle-même).

Il n'y a pas d'obligation de publier les sources modifiées d'un programme sous license Apache, mais le cas échéant, il
faut veiller à:

- Diffuser une copie de la licence avec le code source.
- Mentioner clairement chaque fichier modifié.
- Mentioner les brevets, marques déposées, copyright et note d'attribution.
- Ne pas modifier la license originale.

Mozilla Public License
----------------------

Cette license est plus permissive que la GPL, car elle n'est pas héréditaire : Elle permet d'intégrer des fichiers 
source MPL avec des sources soumis à n'importe quelle autre licence.
