{
    "system": {
        "trusted_domains": ["nextcloud.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}"],
        "overwrite.cli.url": "https:\/\/nextcloud.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}",
        "trusted_proxies": ["172.0.0.0/8"],
        "auth.bruteforce.protection.enabled": false
    }
}
