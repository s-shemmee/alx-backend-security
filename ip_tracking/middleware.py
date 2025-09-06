# IP Tracking Middleware
from django.utils.deprecation import MiddlewareMixin
from .models import RequestLog, BlockedIP
from django.utils import timezone

from django.http import HttpResponseForbidden

import requests
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
			try:
				response = requests.get(f'https://ipinfo.io/{ip}/json')
				if response.status_code == 200:
					geo_data = response.json()
					country = geo_data.get('country', '')
					city = geo_data.get('city', '')
					geo = {'country': country, 'city': city}
					cache.set(geo_cache_key, geo, 60 * 60 * 24)
				else:
					geo = {'country': '', 'city': ''}
			except Exception:
				geo = {'country': '', 'city': ''}
		country = geo.get('country', '')
		city = geo.get('city', '')
		RequestLog.objects.create(
			ip_address=ip,
			timestamp=timezone.now(),
			path=path,
			country=country,
			city=city
		)

