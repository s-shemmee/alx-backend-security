# IP Tracking Middleware
from django.utils.deprecation import MiddlewareMixin
from .models import RequestLog, BlockedIP
from django.utils import timezone

from django.http import HttpResponseForbidden

from ipgeolocation import IpGeolocationAPI
from django.core.cache import cache

class IPLoggingMiddleware(MiddlewareMixin):
	def process_request(self, request):
		ip = request.META.get('REMOTE_ADDR', '')
		path = request.path
		# Block request if IP is blacklisted
		if BlockedIP.objects.filter(ip_address=ip).exists():
			return HttpResponseForbidden('Forbidden: Your IP is blacklisted.')
		# Geolocation caching (24 hours)
		geo_cache_key = f'geo_{ip}'
		geo = cache.get(geo_cache_key)
		if not geo:
			api = IpGeolocationAPI()
			geo_data = api.get_geolocation(ip_address=ip)
			country = geo_data.get('country_name', '')
			city = geo_data.get('city', '')
			geo = {'country': country, 'city': city}
			cache.set(geo_cache_key, geo, 60 * 60 * 24)
		country = geo.get('country', '')
		city = geo.get('city', '')
		RequestLog.objects.create(
			ip_address=ip,
			timestamp=timezone.now(),
			path=path,
			country=country,
			city=city
		)

