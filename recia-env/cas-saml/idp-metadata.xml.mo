<?xml version="1.0" encoding="UTF-8"?>
<EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:shibmd="urn:mace:shibboleth:metadata:1.0" xmlns:xml="http://www.w3.org/XML/1998/namespace" xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui" entityID="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
        <Extensions>
            <shibmd:Scope regexp="false">{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}</shibmd:Scope>
        </Extensions>
        <KeyDescriptor use="signing">
            <ds:KeyInfo>
                <ds:X509Data>
                    <ds:X509Certificate>MIIDKjCCAhKgAwIBAgIVALA8F0B3qcR2Vm1vigb8NaoedklLMA0GCSqGSIb3DQEB
CwUAMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVzdDAeFw0xOTA0MDUxMzE5
NDRaFw0zOTA0MDUxMzE5NDRaMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVz
dDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKi4/m389YzAV2/KShI5
Mglemy1JmBMWy+Gw0+XiU5M3jHvDo7bkRo1Ct09GhjlzLLccTZz8e86GcTvO6Z4B
LlktSRpd6DJY1frGgOzxm2ATFxvbEeb9Z/VyoORxoEImChbj6ipyAeqz6ZY2tQM7
CWyEqezQizLUwry1Zb7kp7ejCI1KdS1/tC6IpmTGytSUsHKxEGxLfnL90j7NXKay
224d6k3ZLjXZQOekKeBLXykxZd6KMJn3GxgWJghzm55jIKYzNKvZ1XLU4V7g/2Nb
j1ckxzi1cbH7qvqBCIWbw222W5u2VRYDCpa5oiBUxnsh39sl7Ez+jQUtCm3Ja2sp
NI0CAwEAAaNhMF8wHQYDVR0OBBYEFAC85/hvGbiOx1UGrZS0ln/O9Bj4MD4GA1Ud
EQQ3MDWCEmNhcy5yZWNpYS1lbnYudGVzdIYfY2FzLnJlY2lhLWVudi50ZXN0L2lk
cC9tZXRhZGF0YTANBgkqhkiG9w0BAQsFAAOCAQEALQYdQmy/ovCGPmD4yxwAv/wo
N+buWIY/zDT7HpPKYOeT10iP24zY9eXe2AxKe2g2CcZg8pHpcSrXieRXc/ahnEE6
NKbVucz8Cx7d43upPuOaSehMNeKxuzrVZ4EgbYjwBVWlO+1HCXgDsynpXggCP2Jr
9Shy6foggVm8WVrY/eBTlMWMX722w5VnLaAs1bpR+yn+IxgAOhKlkBEGzjH4Yn4t
6XYRsClsfa/rI8i0q0SNKHk6AZfPNaGHjbVH1DppfgjUlPEXPs2gW59iFJzD1RPi
y1PjJTc+7uYison7jhGVIS8tvzbRsEGo+k8G4NcIDM1I4ySqgE/+z1hrf9O6Tg==</ds:X509Certificate>
                </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <KeyDescriptor use="encryption">
            <ds:KeyInfo>
                <ds:X509Data>
                    <ds:X509Certificate>MIIDKjCCAhKgAwIBAgIVANv72PpRsJ30NnJK+/lKdr48UhrwMA0GCSqGSIb3DQEB
CwUAMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVzdDAeFw0xOTA0MDUxMzE5
NDRaFw0zOTA0MDUxMzE5NDRaMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVz
dDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKjvSNTLl4pHWKYNvfQv
rEvr7AlOUtWRFpCOHc3AruY0a3j5wtDkbkkBSrsSkYtdo+mGSTo15y9YueXQzIVz
fdQ7BovjMK428zPKoeg332TqHPqONImGnIJ8es54vD+LEgwx+MvxuS1W+x9Wznkz
HdomZRe3FZJckrXGGyiSiBGzKf/E2x8+RGStlB3HuwowVEc+tCh6MYSxv/sGdL6W
HHOHw5Hpn4bsy8OleonVZ2G0niRhFQuH6VPkG6dZ5unSAlC+fHeJJ7IzPFLai+KX
8qVrUm3ywuGjxuByd82ry2bQCJ/YN3AqGZLKyLR4voTk/YjHI7d+jMMWoK7dCHBe
OqsCAwEAAaNhMF8wHQYDVR0OBBYEFOtis2RtXRymk7gas0tv9ocyfLrJMD4GA1Ud
EQQ3MDWCEmNhcy5yZWNpYS1lbnYudGVzdIYfY2FzLnJlY2lhLWVudi50ZXN0L2lk
cC9tZXRhZGF0YTANBgkqhkiG9w0BAQsFAAOCAQEAEPLCLZBb6Cvf6FTajAxo3RU1
RZwIu/N1inIz1aJeeK9vm1Ydkpm0kocEIn5Ren138mx33Rq9KBnUV2YEDuKAy0zw
nJ0jPYpZk7YczgH/ArGbgJajHEPpfv/ZfShp3be5G7MxN5WRFL89rsCudPYdkl3f
5tDAbxf/cxP25qXYsSqYkhrNeTSHQOctuiZB6k3+A7hffsdx/1IONLhXZaLMYwCd
4qX1BfDN2Q5TSyErEYtk0Fxc/0tUHXF0AT5sCjbFtsmjuSI2ud5limTQ5fTD3rHq
GqZjPY8SMwF/RwfQ8/5cU4Kow/7ZXJAAGoYpF6oqdzVCSgiEUXCIAdhUS3JRAA==</ds:X509Certificate>
                </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>

        <!--
        <ArtifactResolutionService Binding="urn:oasis:names:tc:SAML:1.0:bindings:SOAP-binding" 
                                   Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML1/SOAP/ArtifactResolution" index="1"/>
        -->
        
        <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML2/POST/SLO"/>
        
        <NameIDFormat>urn:mace:shibboleth:1.0:nameIdentifier</NameIDFormat>
        <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>

        <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML2/POST/SSO"/>
        <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign" Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML2/POST-SimpleSign/SSO"/>
        <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML2/Redirect/SSO"/>
        <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML2/SOAP/ECP"/>
    </IDPSSODescriptor>

    <!--
    <AttributeAuthorityDescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:1.1:protocol urn:oasis:names:tc:SAML:2.0:protocol">
        <Extensions>
            <shibmd:Scope regexp="false">{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}</shibmd:Scope>
        </Extensions>
        <KeyDescriptor use="signing">
            <ds:KeyInfo>
                <ds:X509Data>
                    <ds:X509Certificate>MIIDKjCCAhKgAwIBAgIVALA8F0B3qcR2Vm1vigb8NaoedklLMA0GCSqGSIb3DQEB
CwUAMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVzdDAeFw0xOTA0MDUxMzE5
NDRaFw0zOTA0MDUxMzE5NDRaMB0xGzAZBgNVBAMMEmNhcy5yZWNpYS1lbnYudGVz
dDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKi4/m389YzAV2/KShI5
Mglemy1JmBMWy+Gw0+XiU5M3jHvDo7bkRo1Ct09GhjlzLLccTZz8e86GcTvO6Z4B
LlktSRpd6DJY1frGgOzxm2ATFxvbEeb9Z/VyoORxoEImChbj6ipyAeqz6ZY2tQM7
CWyEqezQizLUwry1Zb7kp7ejCI1KdS1/tC6IpmTGytSUsHKxEGxLfnL90j7NXKay
224d6k3ZLjXZQOekKeBLXykxZd6KMJn3GxgWJghzm55jIKYzNKvZ1XLU4V7g/2Nb
j1ckxzi1cbH7qvqBCIWbw222W5u2VRYDCpa5oiBUxnsh39sl7Ez+jQUtCm3Ja2sp
NI0CAwEAAaNhMF8wHQYDVR0OBBYEFAC85/hvGbiOx1UGrZS0ln/O9Bj4MD4GA1Ud
EQQ3MDWCEmNhcy5yZWNpYS1lbnYudGVzdIYfY2FzLnJlY2lhLWVudi50ZXN0L2lk
cC9tZXRhZGF0YTANBgkqhkiG9w0BAQsFAAOCAQEALQYdQmy/ovCGPmD4yxwAv/wo
N+buWIY/zDT7HpPKYOeT10iP24zY9eXe2AxKe2g2CcZg8pHpcSrXieRXc/ahnEE6
NKbVucz8Cx7d43upPuOaSehMNeKxuzrVZ4EgbYjwBVWlO+1HCXgDsynpXggCP2Jr
9Shy6foggVm8WVrY/eBTlMWMX722w5VnLaAs1bpR+yn+IxgAOhKlkBEGzjH4Yn4t
6XYRsClsfa/rI8i0q0SNKHk6AZfPNaGHjbVH1DppfgjUlPEXPs2gW59iFJzD1RPi
y1PjJTc+7uYison7jhGVIS8tvzbRsEGo+k8G4NcIDM1I4ySqgE/+z1hrf9O6Tg==</ds:X509Certificate>
                </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <AttributeService Binding="urn:oasis:names:tc:SAML:1.0:bindings:SOAP-binding" Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML1/SOAP/AttributeQuery"/>
        <AttributeService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://cas.{{DOCKER_DEVBOX_DOMAIN_PREFIX}}.{{DOCKER_DEVBOX_DOMAIN}}/cas/idp/profile/SAML2/SOAP/AttributeQuery"/>
    </AttributeAuthorityDescriptor>
    -->
    
    <!--
    <Organization>
        <OrganizationName xml:lang="en">Institution Name</OrganizationName>
        <OrganizationDisplayName xml:lang="en">Institution DisplayName</OrganizationDisplayName>
        <OrganizationURL xml:lang="en">URL</OrganizationURL>
    </Organization>
    <ContactPerson contactType="administrative">
        <GivenName>John Smith</GivenName>
        <EmailAddress>jsmith@example.org</EmailAddress>
    </ContactPerson>
    <ContactPerson contactType="technical">
        <GivenName>John Smith</GivenName>
        <EmailAddress>jsmith@example.org</EmailAddress>
    </ContactPerson>
    <ContactPerson contactType="support">
        <GivenName>IT Services Support</GivenName>
        <EmailAddress>support@example.org</EmailAddress>
    </ContactPerson>
    -->
</EntityDescriptor>
