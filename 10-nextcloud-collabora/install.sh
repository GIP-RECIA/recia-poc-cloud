#!/usr/bin/env bash

occ maintenance:install \
  --admin-user=admin --admin-pass=admin \
  --database=pgsql --database-host=nextcloud-db --database-name=nextcloud \
  --database-user=postgres --database-pass=reciacloud

occ config:import /config/system.config.json

dc exec nextcloud-php occ-import-system-certs

occ app:install user_saml
occ app:install richdocuments
occ app:install files_antivirus
occ app:enable user_ldap
occ app:enable files_external
occ app:enable reciacustom

dc exec nextcloud-php apply-nextcloud-patches

occ config:import /config/user_ldap.config.json
occ config:import /config/user_saml.config.json
occ config:import /config/richdocuments.config.json
occ config:import /config/files_antivirus.config.json

occ maintenance:update:htaccess