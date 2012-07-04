from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from sslutils.utils import build_ssl_http_response
import new


#Copy of django.http.HttpRequest.is_secure from Django 1.4
def is_secure(self):
    # First, check the SECURE_PROXY_SSL_HEADER setting.
    if hasattr(settings, 'SECURE_PROXY_SSL_HEADER'):
        try:
            header, value = settings.SECURE_PROXY_SSL_HEADER
        except ValueError:
            raise ImproperlyConfigured('The SECURE_PROXY_SSL_HEADER setting must be a tuple containing two values.')
        if self.META.get(header, None) == value:
            return True
    # Failing that, fall back to _is_secure(), which is a hook for
    # subclasses to implement.
    return self._is_secure()

class SecureProxySSLHeaderMiddleware(object):
    '''
    Support for reverse proxy is_secure
    '''
    def process_request(self, request, *args, **kwargs):
        request._is_secure = request.is_secure
        request.is_secure = new.instancemethod(is_secure, request, None)
        return None

class ForceSSLMiddleware(object):
    def process_request(self, request, *args, **kwargs):
        if not request.is_secure():
            return build_ssl_http_response(request)
        return None