# no-self-use snippets for cryptography

# File: /root/ecooptimizer/cryptography/src/cryptography/hazmat/backends/openssl/backend.py
# Line: 82

def openssl_assert(self, ok: bool) -> None:
    return binding._openssl_assert(ok)


# ==================================================
# Line: 92

def openssl_version_text(self) -> str:
    """
    Friendly string name of the loaded OpenSSL library. This is not
    necessarily the same version as it was compiled against.

    Example: OpenSSL 3.2.1 30 Jan 2024
    """
    return rust_openssl.openssl_version_text()


# ==================================================
# Line: 101

def openssl_version_number(self) -> int:
    return rust_openssl.openssl_version()


# ==================================================
# Line: 162

def _consume_errors(self) -> list[rust_openssl.OpenSSLError]:
    return rust_openssl.capture_error_stack()


# ==================================================
# Line: 253

def dh_supported(self) -> bool:
    return (
        not rust_openssl.CRYPTOGRAPHY_IS_BORINGSSL
        and not rust_openssl.CRYPTOGRAPHY_IS_AWSLC
    )


# ==================================================
# Line: 295

def pkcs7_supported(self) -> bool:
    return (
        not rust_openssl.CRYPTOGRAPHY_IS_BORINGSSL
        and not rust_openssl.CRYPTOGRAPHY_IS_AWSLC
    )



# ==================================================
# File: /root/ecooptimizer/cryptography/src/cryptography/hazmat/primitives/serialization/ssh.py
# Line: 316

def get_public(
    self, data: memoryview

# ==================================================
# Line: 333

def load_private(
    self, data: memoryview, pubfields, unsafe_skip_rsa_key_validation: bool

# ==================================================
# Line: 357

def encode_public(
    self, public_key: rsa.RSAPublicKey, f_pub: _FragList

# ==================================================
# Line: 365

def encode_private(
    self, private_key: rsa.RSAPrivateKey, f_priv: _FragList

# ==================================================
# Line: 390

def get_public(self, data: memoryview) -> tuple[tuple, memoryview]:
    """DSA public fields"""
    p, data = _get_mpint(data)
    q, data = _get_mpint(data)
    g, data = _get_mpint(data)
    y, data = _get_mpint(data)
    return (p, q, g, y), data


# ==================================================
# Line: 445

def _validate(self, public_numbers: dsa.DSAPublicNumbers) -> None:
    parameter_numbers = public_numbers.parameter_numbers
    if parameter_numbers.p.bit_length() != 1024:
        raise ValueError("SSH supports only 1024 bit DSA keys")



# ==================================================
# Line: 532

def get_public(
    self, data: memoryview

# ==================================================
# Line: 563

def encode_public(
    self, public_key: ed25519.Ed25519PublicKey, f_pub: _FragList

# ==================================================
# Line: 611

def load_public(
    self, data: memoryview

# ==================================================
# Line: 619

def get_public(self, data: memoryview) -> typing.NoReturn:
    # Confusingly `get_public` is an entry point used by private key
    # loading.
    raise UnsupportedAlgorithm(
        "sk-ssh-ed25519 private keys cannot be loaded"
    )



# ==================================================
# Line: 637

def load_public(
    self, data: memoryview

# ==================================================
# Line: 645

def get_public(self, data: memoryview) -> typing.NoReturn:
    # Confusingly `get_public` is an entry point used by private key
    # loading.
    raise UnsupportedAlgorithm(
        "sk-ecdsa-sha2-nistp256 private keys cannot be loaded"
    )



# ==================================================
# File: /root/ecooptimizer/cryptography/src/cryptography/x509/extensions.py
# Line: 1392

def _validate_ip_name(self, tree: Iterable[GeneralName]) -> None:
    if any(
        isinstance(name, IPAddress)
        and not isinstance(
            name.value, (ipaddress.IPv4Network, ipaddress.IPv6Network)
        )
        for name in tree
    ):
        raise TypeError(
            "IPAddress name constraints must be an IPv4Network or"
            " IPv6Network object"
        )


# ==================================================
# Line: 1405

def _validate_dns_name(self, tree: Iterable[GeneralName]) -> None:
    if any(
        isinstance(name, DNSName) and "*" in name.value for name in tree
    ):
        raise ValueError(
            "DNSName name constraints must not contain the '*' wildcard"
            " character"
        )


# ==================================================
