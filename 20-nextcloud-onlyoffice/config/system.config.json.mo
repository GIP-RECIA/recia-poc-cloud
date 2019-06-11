{
    "system": {
        "trusted_domains": ["nextcloud.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}", "nextcloud.1d.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}", "nextcloud.2d.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}"],
        "overwrite.cli.url": "https:\/\/nextcloud.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}",
        "trusted_proxies": ["0.0.0.0/0"],
        "auth.bruteforce.protection.enabled": false,
        "theme": {"/.*\\.1d\\..*/": "1d", "/.*\\.2d\\..*/": "2d"}
    }
}
