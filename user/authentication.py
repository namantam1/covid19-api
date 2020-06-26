import rest_framework.authentication
 
from .models import Token
 
 
class TokenAuthentication(rest_framework.authentication.TokenAuthentication):
    model = Token
    """
    Extend the TokenAuthentication class to support querystring authentication
    in the form of "http://www.example.com/?auth_token=<token_key>"
    """
    def authenticate(self, request):
        # Check if 'token_auth' is in the request query params.
        # Give precedence to 'Authorization' header.
        if 'auth_token' in request.GET and \
                        'HTTP_AUTHORIZATION' not in request.META:
            return self.authenticate_credentials(request.GET.get('auth_token'))
        else:
            return super(TokenAuthentication, self).authenticate(request)