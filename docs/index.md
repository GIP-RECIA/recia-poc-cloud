# Accueil

Expertise et mise en oeuvre de démonstrateurs pour le stockage et l'édition collaborative de documents.

## Introduction

Le GIP RECIA et ses partenaires souhaitent enrichir l'offre de services de l'ENT NetO'centre/Touraine-eschool avec
le souci d'offrir aux populations concernées des services fiables, fonctionnellement riches, ergonomiques, bien 
intégrés et adaptés à leurs pratiques.

Un des nouveaux services identifié concerne le stockage centralisé « dans le nuage » de documents, le partage de
ces documents, l'accès à ces documents sous différentes formes (interface web, application mobile).

Il est souhaité de l'associer à un outil d'édition collaborative en ligne pour les documents bureautique : textes,
tableaux, présentations, ...

Il s'agit de mettre en oeuvre des démonstrateurs regroupant d'une part une solution de stockage de document en mode 
« cloud » et d'autre part une solution d'édition, possiblement collaborative, de documents bureautiques stockés sur 
cette solution.

## Solutions évaluées

2 Solutions de stockage sont comparées:

* [nextcloud](https://nextcloud.com/), fork de owncloud développé en php
* [Seafile](https://www.Seafile.com/), développé en python

2 Solutions d'édition collaborative en ligne sont comparées, dans leur version open source et sous licence libre:

* [Collabora Online Development Edition](https://www.collaboraoffice.com/code/)
* [OnlyOffice Community Edition](https://www.onlyoffice.com/fr/)

!!! note Adhérence avec le SI
    Les solutions d'édition n'ont pas d'adhérence avec le SI, et peuvent être installées sans difficultés 
    particulière sur Nextcloud et sur Seafile. Le choix de la solution d'édition collaborative est donc beaucoup moins 
    impactant en terme d'intégration, il est très simple de passer d'une solution à l'autre.
    
    A l'inverse, le choix d'une solution de stockage doit se faire en toute connaissance de cause pour faciliter 
    l'intégration de l'environnement de l'ENT (CAS, LDAP, Theming en fonction du domain d'accès, etc ...), et il serait 
    difficile de remplacer cette solution par la suite.
    
## Installation des environnements test

Les environnements de tests peuvent être installés via Docker en suivante la [documentation associée](./environnements),
et les fichiers README présents dans le repository github.

## A propos de cette documentation

Cette documentation est construite avec [mkdocs](https://www.mkdocs.org/) à partir de fichiers Markdown présents dans 
le dossier mkdocs du repository le répository [Github](https://github.com/GIP-RECIA/recia-poc-cloud/).
