#!/bin/bash

SERVER_NAME="${SERVER_NAME-seafile}"
SERVER_IP="${SERVER_IP-127.0.0.1}"
FILESERVER_PORT="${FILESERVER_PORT-8082}"
SEAFILE_DIR="${SEAFILE_DIR-${SEAFILE_PATH}/seafile-data}"

USE_EXISTING_DB="${USE_EXISTING_DB-0}"
MYSQL_HOST="${MYSQL_HOST-mysql}"
MYSQL_PORT="${MYSQL_PORT-3306}"

MYSQL_ROOT_PASSWD="${MYSQL_ROOT_PASSWD-${MYSQL_ROOT_PASSWORD}}"

MYSQL_USER="${MYSQL_USER-seafile}"
MYSQL_USER_PASSWD="${MYSQL_USER_PASSWD-${MYSQL_USER}}"
MYSQL_USER_HOST="${MYSQL_USER_HOST-%}"

CCNET_DB="${CCNET_DB-ccnet-db}"
SEAFILE_DB="${SEAFILE_DB-seafile-db}"
SEAHUB_DB="${SEAHUB_DB-seahub-db}"

ADMIN_EMAIL="${ADMIN_EMAIL-admin@example.com}"
ADMIN_PASSWORD="${ADMIN_PASSWORD-admin}"