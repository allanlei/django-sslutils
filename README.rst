Installation
================
.. code-block:: console

    pip install django-sslutils


Usage
=====


Site Wide Blanket Method
========================

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'sslutils.middleware.ForceSSLMiddleware',
    )


Fine Grain Method
=================

.. code-block:: python

    from sslutils.decorators import forcessl

    @forcessl
    def myview(request):
        ...

    @forcessl(redirect_to='http://....', permanent=True)
    def myview(request):
        ...

    urlpatterns = patterns('',
        url(r'^$', forcessl(views.MyView.as_view())),
    )