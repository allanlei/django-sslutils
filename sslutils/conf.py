from django.conf import settings
from appconf import AppConf

class SslUtilsAppConf(AppConf):
    PERMANENT = False

    class Meta:
    	prefix = 'sslutils'