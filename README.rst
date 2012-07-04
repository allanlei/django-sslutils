===============================================
django-crispy-form has replaced django-uni-form
===============================================


We've decided to move development on `django-uni-form` to `django-crispy-forms`_.  From now on, development on `django-uni-form` has been stopped, and any future work will be for security issues only on legacy code. 

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