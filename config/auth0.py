import json
import os

from configurations import Configuration, values
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from six.moves.urllib import request


def get_jwt_auth():
    JWKS_URL = os.environ.get('JWKS_URL')
    json_url = request.urlopen(JWKS_URL)
    jwks = json.loads(json_url.read())
    cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'

    certificate = load_pem_x509_certificate(str.encode(cert), default_backend())

    public_key = certificate.public_key()

    return {
        'JWT_PAYLOAD_GET_USERNAME_HANDLER':
            'auth0authorization.user.jwt_get_username_from_payload_handler',
        'JWT_PUBLIC_KEY': public_key,
        'JWT_SECRET_KEY': os.environ.get('JWT_SECRET_KEY'),  # Auth0 Client Secret
        'JWT_ALGORITHM': 'RS256',
        'JWT_AUDIENCE': os.environ.get('JWT_AUDIENCE'),  # Auth0 Client ID
        'JWT_ISSUER': os.environ.get('JWT_ISSUER'),  # seems to be the tenant
        'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    }