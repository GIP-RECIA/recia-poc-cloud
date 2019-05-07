cas.server.name=https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}
cas.server.prefix=${cas.server.name}/cas

# Configuration for reverse proxy (https://apereo.github.io/2018/11/16/cas60-gettingstarted-overlay/)
server.port=8080
server.ssl.enabled=false

logging.config: file:/etc/cas/config/log4j2.xml
logging.level.org.apereo.cas=DEBUG

cas.serviceRegistry.json.location=file:/etc/cas/services

cas.authn.accept.users=
cas.authn.authenticationAttributeRelease.enabled=true

cas.authn.ldap[0].type=AUTHENTICATED
cas.authn.ldap[0].ldapUrl=ldap://ldap.pce-env
cas.authn.ldap[0].useSsl=false
cas.authn.ldap[0].useStartTls=false
cas.authn.ldap[0].baseDn=dc=esco-centre,dc=fr
cas.authn.ldap[0].searchFilter=(&(|(objectclass=ENTPerson))(|(ENTPersonLogin={user})))
cas.authn.ldap[0].bindDn=cn=admin,ou=administrateurs,dc=esco-centre,dc=fr
cas.authn.ldap[0].bindCredential=admin
cas.authn.ldap[0].principalAttributeList=uid,cn,sn,givenName,displayName,mail,ENTPersonLogin

cas.authn.samlIdp.entityId=https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp
cas.authn.samlIdp.scope={{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}

cas.tgc.crypto.encryption.key=TqKknq1PPCbjsS8vWkfDh3bD4403SfjHUz9ZKeZgOIM
cas.tgc.crypto.signing.key=LHYT5DFvEgqZlbpUn9Uju6r2XQxp48Max207-FS6RLwTrjmoqDh2tnqotrHMUIaOyiLcDBvraBm50qAehDcivg
cas.webflow.crypto.signing.key=Bg8Oj2IC1Jad-p5hg_JjO6LsrTHCYKyXMDOuJAVDWME9kz16hq7NujYzAGLx5374659pTCpZJ_GaIIS9EbmK-Q
cas.webflow.crypto.encryption.key=EtrKpznC08al_MUm8SeQDA
