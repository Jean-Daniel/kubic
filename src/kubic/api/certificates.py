from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class CertificateSigningRequestSpec(KubernetesObject):
    """CertificateSigningRequestSpec contains the certificate request."""

    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"

    _required_ = ["request", "signer_name"]

    expiration_seconds: int
    """
    expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.
    
    The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.
    
    Certificate signers may not honor this field for various reasons:
    
      1. Old signer that is unaware of the field (such as the in-tree
         implementations prior to v1.22)
      2. Signer whose configured maximum is shorter than the requested duration
      3. Signer whose configured minimum is longer than the requested duration
    
    The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.
    """
    extra: dict[str, list[str]]
    """ extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """
    groups: list[str]
    """ groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """
    request: core.Base64
    """ request contains an x509 certificate signing request encoded in a "CERTIFICATE REQUEST" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded. """
    signer_name: str
    """
    signerName indicates the requested signer, and is a qualified name.
    
    List/watch requests for CertificateSigningRequests can filter on this field using a "spec.signerName=NAME" fieldSelector.
    
    Well-known Kubernetes signers are:
     1. "kubernetes.io/kube-apiserver-client": issues client certificates that can be used to authenticate to kube-apiserver.
      Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the "csrsigning" controller in kube-controller-manager.
     2. "kubernetes.io/kube-apiserver-client-kubelet": issues client certificates that kubelets use to authenticate to kube-apiserver.
      Requests for this signer can be auto-approved by the "csrapproving" controller in kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.
     3. "kubernetes.io/kubelet-serving" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.
      Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.
    
    More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers
    
    Custom signerNames can also be specified. The signer defines:
     1. Trust distribution: how trust (CA bundles) are distributed.
     2. Permitted subjects: and behavior when a disallowed subject is requested.
     3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.
     4. Required, permitted, or forbidden key usages / extended key usages.
     5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.
     6. Whether or not requests for CA certificates are allowed.
    """
    uid: str
    """ uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """
    usages: list[str]
    """
    usages specifies a set of key usages requested in the issued certificate.
    
    Requests for TLS client certificates typically request: "digital signature", "key encipherment", "client auth".
    
    Requests for TLS serving certificates typically request: "key encipherment", "digital signature", "server auth".
    
    Valid values are:
     "signing", "digital signature", "content commitment",
     "key encipherment", "key agreement", "data encipherment",
     "cert sign", "crl sign", "encipher only", "decipher only", "any",
     "server auth", "client auth",
     "code signing", "email protection", "s/mime",
     "ipsec end system", "ipsec tunnel", "ipsec user",
     "timestamping", "ocsp signing", "microsoft sgc", "netscape sgc"
    """
    username: str
    """ username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """

    def __init__(
        self,
        expiration_seconds: int = None,
        extra: dict[str, list[str]] = None,
        groups: list[str] = None,
        request: core.Base64 = None,
        signer_name: str = None,
        uid: str = None,
        usages: list[str] = None,
        username: str = None,
    ):
        super().__init__(
            expiration_seconds=expiration_seconds,
            extra=extra,
            groups=groups,
            request=request,
            signer_name=signer_name,
            uid=uid,
            usages=usages,
            username=username,
        )


class CertificateSigningRequest(KubernetesApiResource):
    """
    CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a certificate signing request, and having it asynchronously approved and issued.

    Kubelets use this API to obtain:
     1. client certificates to authenticate to kube-apiserver (with the "kubernetes.io/kube-apiserver-client-kubelet" signerName).
     2. serving certificates for TLS endpoints kube-apiserver can connect to securely (with the "kubernetes.io/kubelet-serving" signerName).

    This API can be used to request client certificates to authenticate to kube-apiserver (with the "kubernetes.io/kube-apiserver-client" signerName), or to obtain certificates from custom non-Kubernetes signers.
    """

    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"
    _api_group_ = "certificates.k8s.io"
    _kind_ = "CertificateSigningRequest"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CertificateSigningRequestSpec
    """ spec contains the certificate request, and is immutable after creation. Only the request, signerName, expirationSeconds, and usages fields can be set on creation. Other fields are derived by Kubernetes and cannot be modified by users. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CertificateSigningRequestSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CertificateSigningRequestCondition(KubernetesObject):
    """CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object"""

    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time. """
    last_update_time: meta.Time
    """ lastUpdateTime is the time of the last update to this condition """
    message: str
    """ message contains a human readable message with details about the request state """
    reason: str
    """ reason indicates a brief reason for the request state """
    status: str
    """ status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown". """
    type: str
    """
    type of the condition. Known conditions are "Approved", "Denied", and "Failed".
    
    An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.
    
    A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.
    
    A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.
    
    Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.
    
    Only one condition of a given type is allowed.
    """

    def __init__(
        self,
        last_transition_time: meta.Time = None,
        last_update_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_transition_time=last_transition_time,
            last_update_time=last_update_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class CertificateSigningRequestStatus(KubernetesObject):
    """CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate."""

    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"

    certificate: core.Base64
    """
    certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.
    
    If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.
    
    Validation requirements:
     1. certificate must contain one or more PEM blocks.
     2. All PEM blocks must have the "CERTIFICATE" label, contain no headers, and the encoded data
      must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280.
     3. Non-PEM content may appear before or after the "CERTIFICATE" PEM blocks and is unvalidated,
      to allow for explanatory text as described in section 5.2 of RFC7468.
    
    If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.
    
    The certificate is encoded in PEM format.
    
    When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:
    
        base64(
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
        )
    """
    conditions: list[CertificateSigningRequestCondition]
    """ conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed". """

    def __init__(self, certificate: core.Base64 = None, conditions: list[CertificateSigningRequestCondition] = None):
        super().__init__(certificate=certificate, conditions=conditions)


class ClusterTrustBundleSpec(KubernetesObject):
    """ClusterTrustBundleSpec contains the signer and trust anchors."""

    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1alpha1"

    _required_ = ["trust_bundle"]

    signer_name: str
    """
    signerName indicates the associated signer, if any.
    
    In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.
    
    If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.
    
    If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.
    
    List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector.
    """
    trust_bundle: str
    """
    trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.
    
    The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.
    
    Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data.
    """

    def __init__(self, signer_name: str = None, trust_bundle: str = None):
        super().__init__(signer_name=signer_name, trust_bundle=trust_bundle)


class ClusterTrustBundle(KubernetesApiResource):
    """
    ClusterTrustBundle is a cluster-scoped container for X.509 trust anchors (root certificates).

    ClusterTrustBundle objects are considered to be readable by any authenticated user in the cluster, because they can be mounted by pods using the `clusterTrustBundle` projection.  All service accounts have read access to ClusterTrustBundles by default.  Users who only have namespace-level access to a cluster can read ClusterTrustBundles by impersonating a serviceaccount that they have access to.

    It can be optionally associated with a particular assigner, in which case it contains one valid set of trust anchors for that signer. Signers may have multiple associated ClusterTrustBundles; each is an independent set of trust anchors for that signer. Admission control is used to enforce that only users with permissions on the signer can create or modify the corresponding bundle.
    """

    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1alpha1"
    _api_group_ = "certificates.k8s.io"
    _kind_ = "ClusterTrustBundle"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ metadata contains the object metadata. """
    spec: ClusterTrustBundleSpec
    """ spec contains the signer (if any) and trust anchors. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ClusterTrustBundleSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)
