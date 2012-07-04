from sslutils.conf import settings
from sslutils.utils import build_ssl_redirect_url, build_ssl_http_response


def forcessl(function=None, redirect_to=None, permanent=settings.SSLUTILS_PERMANENT):
    """
        Decorator to make a view only accessible by SSL.  Usage::

            @forcessl
            def my_view(request):
                # I can assume now that only SSL requests get through
                # ...
    """
    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            if not request.is_secure():
                return build_ssl_http_response(request, url=redirect_to)
            return view_func(request, *args, **kwargs)
        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view

    if function is None:
        return _decorator
    return _decorator(function)