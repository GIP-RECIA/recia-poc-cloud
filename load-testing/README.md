Load testing
============

Tests de charges pour les plateformes NextCloud/OnlyOffice

Ces tests de charges sont écrits avec [Locust](https://locust.io/) en Python.

Prérequis
---------

- Python 3.7
- [pipenv](https://docs.pipenv.org/en/latest/)

Installation
------------

```
pipenv install
```


Execution des tests
-------------------

```
pipenv run locust -f nextcloud.py --host https://nextcloud.pce-cloud-1.asogfi.fr
```

Puis se connecter à http://localhost:8089 pour lancer le test de charge
