from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
import requests
import os

class Auth0Authentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        if not auth:
            return None

        try:
            token = auth.split()[1]
            jwks = requests.get(f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/jwks.json').json()
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = {}
            for key in jwks['keys']:
                if key['kid'] == unverified_header['kid']:
                    rsa_key = {
                        'kty': key['kty'],
                        'kid': key['kid'],
                        'use': key['use'],
                        'n': key['n'],
                        'e': key['e']
                    }
            if rsa_key:
                try:
                    payload = jwt.decode(
                        token,
                        rsa_key,
                        algorithms=['RS256'],
                        audience=os.getenv('AUTH0_AUDIENCE'),
                        issuer=f'https://{os.getenv("AUTH0_DOMAIN")}/'
                    )
                    return (None, payload)
                except jwt.ExpiredSignatureError:
                    raise AuthenticationFailed('Token is expired')
                except jwt.JWTClaimsError:
                    raise AuthenticationFailed('Invalid claims')
                except Exception:
                    raise AuthenticationFailed('Invalid token')
        except Exception:
            raise AuthenticationFailed('Invalid authorization header')
        return None