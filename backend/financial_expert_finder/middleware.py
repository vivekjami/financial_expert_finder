from django.http import JsonResponse
import jwt
import requests
from django.conf import settings
from django.contrib.auth import login
from users.models import User

class Auth0Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                jwks = requests.get(f'https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json').json()
                public_key = None
                for key in jwks['keys']:
                    if key['kid'] == jwt.get_unverified_header(token)['kid']:
                        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
                        break
                if not public_key:
                    return JsonResponse({'error': 'Public key not found'}, status=401)

                payload = jwt.decode(
                    token,
                    public_key,
                    algorithms=['RS256'],
                    audience=settings.AUTH0_CLIENT_ID,
                    issuer=f'https://{settings.AUTH0_DOMAIN}/'
                )
                # Sync Auth0 user with Django user
                user, created = User.objects.get_or_create(
                    email=payload['email'],
                    defaults={'role': 'business'}  # Default role, adjust as needed
                )
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            except jwt.PyJWTError as e:
                return JsonResponse({'error': f'Invalid token: {str(e)}'}, status=401)
        response = self.get_response(request)
        return response