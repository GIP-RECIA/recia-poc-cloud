#!/bin/sh
set -eu

chown -R www-data:root /var/www/html/custom_apps
/entrypoint.sh "$@"
