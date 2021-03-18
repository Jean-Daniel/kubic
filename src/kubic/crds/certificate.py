from typing import List

from .. import KubernetesObject, KubernetesApiResource
from .. import meta


class IssuerRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    group: str
    kind: str
    name: str

    def __init__(self, group: str = None, kind: str = None, name: str = None):
        super().__init__(group=group, kind=kind, name=name)


class PasswordSecretRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    key: str
    name: str

    def __init__(self, key: str = None, name: str = None):
        super().__init__(key=key, name=name)


class JKS(KubernetesObject):
    __slots__ = ()

    _required_ = ["create", "password_secret_ref"]

    create: bool
    password_secret_ref: PasswordSecretRef

    def __init__(
        self, create: bool = None, password_secret_ref: PasswordSecretRef = None
    ):
        super().__init__(create=create, password_secret_ref=password_secret_ref)


class Pkcs12(KubernetesObject):
    __slots__ = ()

    _required_ = ["create", "password_secret_ref"]

    create: bool
    password_secret_ref: PasswordSecretRef

    def __init__(
        self, create: bool = None, password_secret_ref: PasswordSecretRef = None
    ):
        super().__init__(create=create, password_secret_ref=password_secret_ref)


class Keystore(KubernetesObject):
    __slots__ = ()

    jks: JKS
    pkcs12: Pkcs12

    def __init__(self, jks: JKS = None, pkcs12: Pkcs12 = None):
        super().__init__(jks=jks, pkcs12=pkcs12)


class PrivateKey(KubernetesObject):
    __slots__ = ()

    algorithm: str
    encoding: str
    rotation_policy: str
    size: int

    def __init__(
        self,
        algorithm: str = None,
        encoding: str = None,
        rotation_policy: str = None,
        size: int = None,
    ):
        super().__init__(
            algorithm=algorithm,
            encoding=encoding,
            rotation_policy=rotation_policy,
            size=size,
        )


class Subject(KubernetesObject):
    __slots__ = ()

    countries: List[str]
    localities: List[str]
    organizational_units: List[str]
    organizations: List[str]
    postal_codes: List[str]
    provinces: List[str]
    serial_number: str
    street_addresses: List[str]

    def __init__(
        self,
        countries: List[str] = None,
        localities: List[str] = None,
        organizational_units: List[str] = None,
        organizations: List[str] = None,
        postal_codes: List[str] = None,
        provinces: List[str] = None,
        serial_number: str = None,
        street_addresses: List[str] = None,
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


class Spec(KubernetesObject):
    __slots__ = ()

    _required_ = ["issuer_ref", "secret_name"]

    _field_names_ = {
        "is_ca": "isCA",
    }
    _revfield_names_ = {
        "isCA": "is_ca",
    }

    common_name: str
    dns_names: List[str]
    duration: str
    email_addresses: List[str]
    encode_usages_in_request: bool
    ip_addresses: List[str]
    is_ca: bool
    issuer_ref: IssuerRef
    keystores: Keystore
    private_key: PrivateKey
    renew_before: str
    secret_name: str
    subject: Subject
    uris: List[str]
    usages: List[str]

    def __init__(
        self,
        common_name: str = None,
        dns_names: List[str] = None,
        duration: str = None,
        email_addresses: List[str] = None,
        encode_usages_in_request: bool = None,
        ip_addresses: List[str] = None,
        is_ca: bool = None,
        issuer_ref: IssuerRef = None,
        keystores: Keystore = None,
        private_key: PrivateKey = None,
        renew_before: str = None,
        secret_name: str = None,
        subject: Subject = None,
        uris: List[str] = None,
        usages: List[str] = None,
    ):
        super().__init__(
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
            secret_name=secret_name,
            subject=subject,
            uris=uris,
            usages=usages,
        )


class Certificate(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cert-manager.io"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: Spec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: Spec = None,
    ):
        super().__init__(
            "cert-manager.io/v1",
            "Certificate",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


New = Certificate
