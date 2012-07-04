from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect

from sslutils.conf import settings


def build_ssl_redirect_url(request):
	request_url = request.build_absolute_uri(request.get_full_path())
	redirect_url = request_url.replace('http://', 'https://')
	return redirect_url

def build_ssl_http_response(request, url=None):
	redirect_url = url if url is not None else build_ssl_redirect_url(request)
	if settings.SSLUTILS_PERMANENT:
		return HttpResponsePermanentRedirect(redirect_url)
	return HttpResponseRedirect(redirect_url)