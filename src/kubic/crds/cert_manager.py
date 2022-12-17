import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from ..api import core, meta


class SecretRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    key: str
    name: str

    def __init__(self, key: str = None, name: str = None):
        super().__init__(key=key, name=name)


class ExternalAccountBinding(KubernetesObject):
    __slots__ = ()

    _required_ = ["key_id", "key_secret_ref"]

    _field_names_ = {
        "key_id": "keyID",
    }
    _revfield_names_ = {
        "keyID": "key_id",
    }

    key_algorithm: str
    key_id: str
    key_secret_ref: SecretRef

    def __init__(self, key_algorithm: str = None, key_id: str = None, key_secret_ref: SecretRef = None):
        super().__init__(key_algorithm=key_algorithm, key_id=key_id, key_secret_ref=key_secret_ref)


class AcmeDNS(KubernetesObject):
    __slots__ = ()

    _required_ = ["account_secret_ref", "host"]

    account_secret_ref: SecretRef
    host: str

    def __init__(self, account_secret_ref: SecretRef = None, host: str = None):
        super().__init__(account_secret_ref=account_secret_ref, host=host)


class Akamai(KubernetesObject):
    __slots__ = ()

    _required_ = ["access_token_secret_ref", "client_secret_secret_ref", "client_token_secret_ref", "service_consumer_domain"]

    access_token_secret_ref: SecretRef
    client_secret_secret_ref: SecretRef
    client_token_secret_ref: SecretRef
    service_consumer_domain: str

    def __init__(
        self,
        access_token_secret_ref: SecretRef = None,
        client_secret_secret_ref: SecretRef = None,
        client_token_secret_ref: SecretRef = None,
        service_consumer_domain: str = None,
    ):
        super().__init__(
            access_token_secret_ref=access_token_secret_ref,
            client_secret_secret_ref=client_secret_secret_ref,
            client_token_secret_ref=client_token_secret_ref,
            service_consumer_domain=service_consumer_domain,
        )


class ManagedIdentity(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "client_id": "clientID",
        "resource_id": "resourceID",
    }
    _revfield_names_ = {
        "clientID": "client_id",
        "resourceID": "resource_id",
    }

    client_id: str
    resource_id: str

    def __init__(self, client_id: str = None, resource_id: str = None):
        super().__init__(client_id=client_id, resource_id=resource_id)


class AzureDNS(KubernetesObject):
    __slots__ = ()

    _required_ = ["resource_group_name", "subscription_id"]

    _field_names_ = {
        "client_id": "clientID",
        "subscription_id": "subscriptionID",
        "tenant_id": "tenantID",
    }
    _revfield_names_ = {
        "clientID": "client_id",
        "subscriptionID": "subscription_id",
        "tenantID": "tenant_id",
    }

    client_id: str
    client_secret_secret_ref: SecretRef
    environment: str
    hosted_zone_name: str
    managed_identity: ManagedIdentity
    resource_group_name: str
    subscription_id: str
    tenant_id: str

    def __init__(
        self,
        client_id: str = None,
        client_secret_secret_ref: SecretRef = None,
        environment: str = None,
        hosted_zone_name: str = None,
        managed_identity: ManagedIdentity = None,
        resource_group_name: str = None,
        subscription_id: str = None,
        tenant_id: str = None,
    ):
        super().__init__(
            client_id=client_id,
            client_secret_secret_ref=client_secret_secret_ref,
            environment=environment,
            hosted_zone_name=hosted_zone_name,
            managed_identity=managed_identity,
            resource_group_name=resource_group_name,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
        )


class CloudDNS(KubernetesObject):
    __slots__ = ()

    _required_ = ["project"]

    hosted_zone_name: str
    project: str
    service_account_secret_ref: SecretRef

    def __init__(self, hosted_zone_name: str = None, project: str = None, service_account_secret_ref: SecretRef = None):
        super().__init__(hosted_zone_name=hosted_zone_name, project=project, service_account_secret_ref=service_account_secret_ref)


class Cloudflare(KubernetesObject):
    __slots__ = ()

    api_key_secret_ref: SecretRef
    api_token_secret_ref: SecretRef
    email: str

    def __init__(self, api_key_secret_ref: SecretRef = None, api_token_secret_ref: SecretRef = None, email: str = None):
        super().__init__(api_key_secret_ref=api_key_secret_ref, api_token_secret_ref=api_token_secret_ref, email=email)


class Digitalocean(KubernetesObject):
    __slots__ = ()

    _required_ = ["token_secret_ref"]

    token_secret_ref: SecretRef

    def __init__(self, token_secret_ref: SecretRef = None):
        super().__init__(token_secret_ref=token_secret_ref)


class RFC2136(KubernetesObject):
    __slots__ = ()

    _required_ = ["nameserver"]

    nameserver: str
    tsig_algorithm: str
    tsig_key_name: str
    tsig_secret_secret_ref: SecretRef

    def __init__(
        self, nameserver: str = None, tsig_algorithm: str = None, tsig_key_name: str = None, tsig_secret_secret_ref: SecretRef = None
    ):
        super().__init__(
            nameserver=nameserver, tsig_algorithm=tsig_algorithm, tsig_key_name=tsig_key_name, tsig_secret_secret_ref=tsig_secret_secret_ref
        )


class Route53(KubernetesObject):
    __slots__ = ()

    _required_ = ["region"]

    _field_names_ = {
        "access_key_id": "accessKeyID",
        "hosted_zone_id": "hostedZoneID",
    }
    _revfield_names_ = {
        "accessKeyID": "access_key_id",
        "hostedZoneID": "hosted_zone_id",
    }

    access_key_id: str
    hosted_zone_id: str
    region: str
    role: str
    secret_access_key_secret_ref: SecretRef

    def __init__(
        self,
        access_key_id: str = None,
        hosted_zone_id: str = None,
        region: str = None,
        role: str = None,
        secret_access_key_secret_ref: SecretRef = None,
    ):
        super().__init__(
            access_key_id=access_key_id,
            hosted_zone_id=hosted_zone_id,
            region=region,
            role=role,
            secret_access_key_secret_ref=secret_access_key_secret_ref,
        )


class Webhook(KubernetesObject):
    __slots__ = ()

    _required_ = ["group_name", "solver_name"]

    config: t.Any
    group_name: str
    solver_name: str

    def __init__(self, config: t.Any = None, group_name: str = None, solver_name: str = None):
        super().__init__(config=config, group_name=group_name, solver_name=solver_name)


class Dns01(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "acme_dns": "acmeDNS",
        "azure_dns": "azureDNS",
        "cloud_dns": "cloudDNS",
    }
    _revfield_names_ = {
        "acmeDNS": "acme_dns",
        "azureDNS": "azure_dns",
        "cloudDNS": "cloud_dns",
    }

    acme_dns: AcmeDNS
    akamai: Akamai
    azure_dns: AzureDNS
    cloud_dns: CloudDNS
    cloudflare: Cloudflare
    cname_strategy: str
    digitalocean: Digitalocean
    rfc2136: RFC2136
    route53: Route53
    webhook: Webhook

    def __init__(
        self,
        acme_dns: AcmeDNS = None,
        akamai: Akamai = None,
        azure_dns: AzureDNS = None,
        cloud_dns: CloudDNS = None,
        cloudflare: Cloudflare = None,
        cname_strategy: str = None,
        digitalocean: Digitalocean = None,
        rfc2136: RFC2136 = None,
        route53: Route53 = None,
        webhook: Webhook = None,
    ):
        super().__init__(
            acme_dns=acme_dns,
            akamai=akamai,
            azure_dns=azure_dns,
            cloud_dns=cloud_dns,
            cloudflare=cloudflare,
            cname_strategy=cname_strategy,
            digitalocean=digitalocean,
            rfc2136=rfc2136,
            route53=route53,
            webhook=webhook,
        )


class GatewayHTTPRoute(KubernetesObject):
    __slots__ = ()

    labels: dict[str, str]
    service_type: str

    def __init__(self, labels: dict[str, str] = None, service_type: str = None):
        super().__init__(labels=labels, service_type=service_type)


class Metadata(KubernetesObject):
    __slots__ = ()

    annotations: dict[str, str]
    labels: dict[str, str]

    def __init__(self, annotations: dict[str, str] = None, labels: dict[str, str] = None):
        super().__init__(annotations=annotations, labels=labels)


class IngressTemplate(KubernetesObject):
    __slots__ = ()

    metadata: Metadata

    def __init__(self, metadata: Metadata = None):
        super().__init__(metadata=metadata)


class PodTemplateSpec(KubernetesObject):
    __slots__ = ()

    affinity: core.Affinity
    node_selector: dict[str, str]
    priority_class_name: str
    service_account_name: str
    tolerations: list[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        node_selector: dict[str, str] = None,
        priority_class_name: str = None,
        service_account_name: str = None,
        tolerations: list[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            node_selector=node_selector,
            priority_class_name=priority_class_name,
            service_account_name=service_account_name,
            tolerations=tolerations,
        )


class PodTemplate(KubernetesObject):
    __slots__ = ()

    metadata: Metadata
    spec: PodTemplateSpec

    def __init__(self, metadata: Metadata = None, spec: PodTemplateSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class Ingress(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "class": "class_",
    }

    class_: str
    ingress_template: IngressTemplate
    name: str
    pod_template: PodTemplate
    service_type: str

    def __init__(
        self,
        class_: str = None,
        ingress_template: IngressTemplate = None,
        name: str = None,
        pod_template: PodTemplate = None,
        service_type: str = None,
    ):
        super().__init__(class_=class_, ingress_template=ingress_template, name=name, pod_template=pod_template, service_type=service_type)


class Http01(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "gateway_http_route": "gatewayHTTPRoute",
    }
    _revfield_names_ = {
        "gatewayHTTPRoute": "gateway_http_route",
    }

    gateway_http_route: GatewayHTTPRoute
    ingress: Ingress

    def __init__(self, gateway_http_route: GatewayHTTPRoute = None, ingress: Ingress = None):
        super().__init__(gateway_http_route=gateway_http_route, ingress=ingress)


class Selector(KubernetesObject):
    __slots__ = ()

    dns_names: list[str]
    dns_zones: list[str]
    match_labels: dict[str, str]

    def __init__(self, dns_names: list[str] = None, dns_zones: list[str] = None, match_labels: dict[str, str] = None):
        super().__init__(dns_names=dns_names, dns_zones=dns_zones, match_labels=match_labels)


class Solver(KubernetesObject):
    __slots__ = ()

    dns01: Dns01
    http01: Http01
    selector: Selector

    def __init__(self, dns01: Dns01 = None, http01: Http01 = None, selector: Selector = None):
        super().__init__(dns01=dns01, http01=http01, selector=selector)


class Acme(KubernetesObject):
    __slots__ = ()

    _required_ = ["private_key_secret_ref", "server"]

    _field_names_ = {
        "skip_tls_verify": "skipTLSVerify",
    }
    _revfield_names_ = {
        "skipTLSVerify": "skip_tls_verify",
    }

    disable_account_key_generation: bool
    email: str
    enable_duration_feature: bool
    external_account_binding: ExternalAccountBinding
    preferred_chain: str
    private_key_secret_ref: SecretRef
    server: str
    skip_tls_verify: bool
    solvers: list[Solver]

    def __init__(
        self,
        disable_account_key_generation: bool = None,
        email: str = None,
        enable_duration_feature: bool = None,
        external_account_binding: ExternalAccountBinding = None,
        preferred_chain: str = None,
        private_key_secret_ref: SecretRef = None,
        server: str = None,
        skip_tls_verify: bool = None,
        solvers: list[Solver] = None,
    ):
        super().__init__(
            disable_account_key_generation=disable_account_key_generation,
            email=email,
            enable_duration_feature=enable_duration_feature,
            external_account_binding=external_account_binding,
            preferred_chain=preferred_chain,
            private_key_secret_ref=private_key_secret_ref,
            server=server,
            skip_tls_verify=skip_tls_verify,
            solvers=solvers,
        )


class AdditionalOutputFormat(KubernetesObject):
    __slots__ = ()

    _required_ = ["type"]

    type: str

    def __init__(self, type: str = None):
        super().__init__(type=type)


class AppRole(KubernetesObject):
    __slots__ = ()

    _required_ = ["path", "role_id", "secret_ref"]

    path: str
    role_id: str
    secret_ref: SecretRef

    def __init__(self, path: str = None, role_id: str = None, secret_ref: SecretRef = None):
        super().__init__(path=path, role_id=role_id, secret_ref=secret_ref)


class Kubernete(KubernetesObject):
    __slots__ = ()

    _required_ = ["role", "secret_ref"]

    mount_path: str
    role: str
    secret_ref: SecretRef

    def __init__(self, mount_path: str = None, role: str = None, secret_ref: SecretRef = None):
        super().__init__(mount_path=mount_path, role=role, secret_ref=secret_ref)


class Auth(KubernetesObject):
    __slots__ = ()

    app_role: AppRole
    kubernetes: Kubernete
    token_secret_ref: SecretRef

    def __init__(self, app_role: AppRole = None, kubernetes: Kubernete = None, token_secret_ref: SecretRef = None):
        super().__init__(app_role=app_role, kubernetes=kubernetes, token_secret_ref=token_secret_ref)


class CA(KubernetesObject):
    __slots__ = ()

    _required_ = ["secret_name"]

    crl_distribution_points: list[str]
    ocsp_servers: list[str]
    secret_name: str

    def __init__(self, crl_distribution_points: list[str] = None, ocsp_servers: list[str] = None, secret_name: str = None):
        super().__init__(crl_distribution_points=crl_distribution_points, ocsp_servers=ocsp_servers, secret_name=secret_name)


class IssuerRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    group: str
    kind: str
    name: str

    def __init__(self, group: str = None, kind: str = None, name: str = None):
        super().__init__(group=group, kind=kind, name=name)


class JKS(KubernetesObject):
    __slots__ = ()

    _required_ = ["create", "password_secret_ref"]

    create: bool
    password_secret_ref: SecretRef

    def __init__(self, create: bool = None, password_secret_ref: SecretRef = None):
        super().__init__(create=create, password_secret_ref=password_secret_ref)


class PKCS12(KubernetesObject):
    __slots__ = ()

    _required_ = ["create", "password_secret_ref"]

    create: bool
    password_secret_ref: SecretRef

    def __init__(self, create: bool = None, password_secret_ref: SecretRef = None):
        super().__init__(create=create, password_secret_ref=password_secret_ref)


class Keystore(KubernetesObject):
    __slots__ = ()

    jks: JKS
    pkcs12: PKCS12

    def __init__(self, jks: JKS = None, pkcs12: PKCS12 = None):
        super().__init__(jks=jks, pkcs12=pkcs12)


class PrivateKey(KubernetesObject):
    __slots__ = ()

    algorithm: str
    encoding: str
    rotation_policy: str
    size: int

    def __init__(self, algorithm: str = None, encoding: str = None, rotation_policy: str = None, size: int = None):
        super().__init__(algorithm=algorithm, encoding=encoding, rotation_policy=rotation_policy, size=size)


class SecretTemplate(KubernetesObject):
    __slots__ = ()

    annotations: dict[str, str]
    labels: dict[str, str]

    def __init__(self, annotations: dict[str, str] = None, labels: dict[str, str] = None):
        super().__init__(annotations=annotations, labels=labels)


class Subject(KubernetesObject):
    __slots__ = ()

    countries: list[str]
    localities: list[str]
    organizational_units: list[str]
    organizations: list[str]
    postal_codes: list[str]
    provinces: list[str]
    serial_number: str
    street_addresses: list[str]

    def __init__(
        self,
        countries: list[str] = None,
        localities: list[str] = None,
        organizational_units: list[str] = None,
        organizations: list[str] = None,
        postal_codes: list[str] = None,
        provinces: list[str] = None,
        serial_number: str = None,
        street_addresses: list[str] = None,
    ):
        super().__init__(
            countries=countries,
            localities=localities,
            organizational_units=organizational_units,
            organizations=organizations,
            postal_codes=postal_codes,
            provinces=provinces,
            serial_number=serial_number,
            street_addresses=street_addresses,
        )


class CertificateSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["issuer_ref", "secret_name"]

    _field_names_ = {
        "is_ca": "isCA",
    }
    _revfield_names_ = {
        "isCA": "is_ca",
    }

    additional_output_formats: list[AdditionalOutputFormat]
    common_name: str
    dns_names: list[str]
    duration: str
    email_addresses: list[str]
    encode_usages_in_request: bool
    ip_addresses: list[str]
    is_ca: bool
    issuer_ref: IssuerRef
    keystores: Keystore
    private_key: PrivateKey
    renew_before: str
    revision_history_limit: int
    secret_name: str
    secret_template: SecretTemplate
    subject: Subject
    uris: list[str]
    usages: list[str]

    def __init__(
        self,
        additional_output_formats: list[AdditionalOutputFormat] = None,
        common_name: str = None,
        dns_names: list[str] = None,
        duration: str = None,
        email_addresses: list[str] = None,
        encode_usages_in_request: bool = None,
        ip_addresses: list[str] = None,
        is_ca: bool = None,
        issuer_ref: IssuerRef = None,
        keystores: Keystore = None,
        private_key: PrivateKey = None,
        renew_before: str = None,
        revision_history_limit: int = None,
        secret_name: str = None,
        secret_template: SecretTemplate = None,
        subject: Subject = None,
        uris: list[str] = None,
        usages: list[str] = None,
    ):
        super().__init__(
            additional_output_formats=additional_output_formats,
            common_name=common_name,
            dns_names=dns_names,
            duration=duration,
            email_addresses=email_addresses,
            encode_usages_in_request=encode_usages_in_request,
            ip_addresses=ip_addresses,
            is_ca=is_ca,
            issuer_ref=issuer_ref,
            keystores=keystores,
            private_key=private_key,
            renew_before=renew_before,
            revision_history_limit=revision_history_limit,
            secret_name=secret_name,
            secret_template=secret_template,
            subject=subject,
            uris=uris,
            usages=usages,
        )


class Certificate(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cert-manager.io/v1"
    _kind_ = "Certificate"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CertificateSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CertificateSpec = None):
        super().__init__("cert-manager.io/v1", "Certificate", name, namespace, metadata=metadata, spec=spec)


class CertificateRequestSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["issuer_ref", "request"]

    _field_names_ = {
        "is_ca": "isCA",
    }
    _revfield_names_ = {
        "isCA": "is_ca",
    }

    duration: str
    extra: dict[str, list[str]]
    groups: list[str]
    is_ca: bool
    issuer_ref: IssuerRef
    request: core.Base64
    uid: str
    usages: list[str]
    username: str

    def __init__(
        self,
        duration: str = None,
        extra: dict[str, list[str]] = None,
        groups: list[str] = None,
        is_ca: bool = None,
        issuer_ref: IssuerRef = None,
        request: core.Base64 = None,
        uid: str = None,
        usages: list[str] = None,
        username: str = None,
    ):
        super().__init__(
            duration=duration,
            extra=extra,
            groups=groups,
            is_ca=is_ca,
            issuer_ref=issuer_ref,
            request=request,
            uid=uid,
            usages=usages,
            username=username,
        )


class CertificateRequest(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cert-manager.io/v1"
    _kind_ = "CertificateRequest"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CertificateRequestSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CertificateRequestSpec = None):
        super().__init__("cert-manager.io/v1", "CertificateRequest", name, namespace, metadata=metadata, spec=spec)


class ChallengeSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["authorization_url", "dns_name", "issuer_ref", "key", "solver", "token", "type", "url"]

    _field_names_ = {
        "authorization_url": "authorizationURL",
    }
    _revfield_names_ = {
        "authorizationURL": "authorization_url",
    }

    authorization_url: str
    dns_name: str
    issuer_ref: IssuerRef
    key: str
    solver: Solver
    token: str
    type: str
    url: str
    wildcard: bool

    def __init__(
        self,
        authorization_url: str = None,
        dns_name: str = None,
        issuer_ref: IssuerRef = None,
        key: str = None,
        solver: Solver = None,
        token: str = None,
        type: str = None,
        url: str = None,
        wildcard: bool = None,
    ):
        super().__init__(
            authorization_url=authorization_url,
            dns_name=dns_name,
            issuer_ref=issuer_ref,
            key=key,
            solver=solver,
            token=token,
            type=type,
            url=url,
            wildcard=wildcard,
        )


class Challenge(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "acme.cert-manager.io/v1"
    _kind_ = "Challenge"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: ChallengeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ChallengeSpec = None):
        super().__init__("acme.cert-manager.io/v1", "Challenge", name, namespace, metadata=metadata, spec=spec)


class Cloud(KubernetesObject):
    __slots__ = ()

    _required_ = ["api_token_secret_ref"]

    api_token_secret_ref: SecretRef
    url: str

    def __init__(self, api_token_secret_ref: SecretRef = None, url: str = None):
        super().__init__(api_token_secret_ref=api_token_secret_ref, url=url)


class SelfSigned(KubernetesObject):
    __slots__ = ()

    crl_distribution_points: list[str]

    def __init__(self, crl_distribution_points: list[str] = None):
        super().__init__(crl_distribution_points=crl_distribution_points)


class Vault(KubernetesObject):
    __slots__ = ()

    _required_ = ["auth", "path", "server"]

    auth: Auth
    ca_bundle: core.Base64
    namespace: str
    path: str
    server: str

    def __init__(self, auth: Auth = None, ca_bundle: core.Base64 = None, namespace: str = None, path: str = None, server: str = None):
        super().__init__(auth=auth, ca_bundle=ca_bundle, namespace=namespace, path=path, server=server)


class CredentialsRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class TPP(KubernetesObject):
    __slots__ = ()

    _required_ = ["credentials_ref", "url"]

    ca_bundle: core.Base64
    credentials_ref: CredentialsRef
    url: str

    def __init__(self, ca_bundle: core.Base64 = None, credentials_ref: CredentialsRef = None, url: str = None):
        super().__init__(ca_bundle=ca_bundle, credentials_ref=credentials_ref, url=url)


class Venafi(KubernetesObject):
    __slots__ = ()

    _required_ = ["zone"]

    cloud: Cloud
    tpp: TPP
    zone: str

    def __init__(self, cloud: Cloud = None, tpp: TPP = None, zone: str = None):
        super().__init__(cloud=cloud, tpp=tpp, zone=zone)


class IssuerSpec(KubernetesObject):
    __slots__ = ()

    acme: Acme
    ca: CA
    self_signed: SelfSigned
    vault: Vault
    venafi: Venafi

    def __init__(self, acme: Acme = None, ca: CA = None, self_signed: SelfSigned = None, vault: Vault = None, venafi: Venafi = None):
        super().__init__(acme=acme, ca=ca, self_signed=self_signed, vault=vault, venafi=venafi)


class ClusterIssuer(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cert-manager.io/v1"
    _kind_ = "ClusterIssuer"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: IssuerSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: IssuerSpec = None):
        super().__init__("cert-manager.io/v1", "ClusterIssuer", name, "", metadata=metadata, spec=spec)


class Issuer(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cert-manager.io/v1"
    _kind_ = "Issuer"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: IssuerSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: IssuerSpec = None):
        super().__init__("cert-manager.io/v1", "Issuer", name, namespace, metadata=metadata, spec=spec)


class OrderSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["issuer_ref", "request"]

    common_name: str
    dns_names: list[str]
    duration: str
    ip_addresses: list[str]
    issuer_ref: IssuerRef
    request: core.Base64

    def __init__(
        self,
        common_name: str = None,
        dns_names: list[str] = None,
        duration: str = None,
        ip_addresses: list[str] = None,
        issuer_ref: IssuerRef = None,
        request: core.Base64 = None,
    ):
        super().__init__(
            common_name=common_name,
            dns_names=dns_names,
            duration=duration,
            ip_addresses=ip_addresses,
            issuer_ref=issuer_ref,
            request=request,
        )


class Order(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "acme.cert-manager.io/v1"
    _kind_ = "Order"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: OrderSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: OrderSpec = None):
        super().__init__("acme.cert-manager.io/v1", "Order", name, namespace, metadata=metadata, spec=spec)
