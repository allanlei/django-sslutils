## Requirements
```
django-appconf >= 0.5
```

## Installation
```console
pip install django-sslutils
```

# Important Notes
**django-sslutils requires that `request.is_secure()` works correctly/intended**.

`request.is_secure()` works not quite as intended when you use Django behind a reverse proxy. 
Django looks for certain HTTP headers, and when behind a reverse proxy, those headers are usually stripped away and replaced with something else like `X-FORWARDED-PROTO https`.
To "fix" this, there are a couple methods.

Also take a look at Django's documentation on the [SECURE_PROXY_SSL_HEADER](https://docs.djangoproject.com/en/1.4/ref/settings/#secure-proxy-ssl-header) setting.
Their suggestions applies for the other solutions too.

*Please replace `X-FORWARED-PROTO` and `https` with the appropriate header/value. `X-FORWARDED-PROTO` and `https` is what works for Django/gunicorn on Heorku.*


#### Django with gunicorn
Run gunicorn with config
```python
secure_scheme_headers = {
    'X-FORWARDED-PROTO': 'https',
}
```

#### Django >= 1.4
settings.py
```python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

#### sslutils.middleware.SecureProxySSLHeaderMiddleware (Not recommended)
This is meant for Django < 1.4 since they dont have support for the `SECURE_PROXY_SSL_HEADER`. 
This middleware preserves `request.is_secure` by moving it to `request._is_secure` and replacing it with a method that checks the `SECURE_PROXY_SSL_HEADER` setting.
The implemented function is an exact copy from Django 1.4. See source to see what happens.


Please read:
* [SECURE_PROXY_SSL_HEADER](https://docs.djangoproject.com/en/1.4/ref/settings/#secure-proxy-ssl-header)
* [How to make python on Heroku https only?](http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only/9204892#9204892)


## Usage

### Site Wide Blanket Method
This method will force SSL on all incoming URLs. This is probably the most common use case.
```python
MIDDLEWARE_CLASSES = (
    'sslutils.middleware.ForceSSLMiddleware',
)
```

### Fine Grain Method
With this method you can specify which URLs/views require SSL with the use of decorators

###### View function with no options
```python
from sslutils.decorators import forcessl

@forcessl
def myview(request):
    ...
```

###### View function with options
* `redirect_to` is a URL to redirect to on a non-SSL request. If set to `None` it will use the requested URL(default).
* `permanent` See `SSLUTILS_PERMANENT` below.

```python
from sslutils.decorators import forcessl

@forcessl(redirect_to='http://....', permanent=True)
def myview(request):
    ...
```

###### Decorating a Class Based View
```python
from sslutils.decorators import forcessl

urlpatterns = patterns('',
    url(r'^$', forcessl(views.MyView.as_view())),
)
```

## Configuration
##### SSLUTILS_PERMANENT (True/False, default: False)
This sets whether to return a Http 301 or Http 302 response. django-sslutils does not set the status codes on the responses, rather, it uses either HttpResponseRedirect or HttpResponsePermanentRedirect.