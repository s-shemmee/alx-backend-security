# Models for IP Tracking
from django.db import models

class RequestLog(models.Model):
	ip_address = models.GenericIPAddressField()
	timestamp = models.DateTimeField(auto_now_add=True)
	path = models.CharField(max_length=255)
	country = models.CharField(max_length=64, blank=True, null=True)
	city = models.CharField(max_length=64, blank=True, null=True)

	def __str__(self):
		return f"{self.ip_address} @ {self.timestamp} -> {self.path}"

class BlockedIP(models.Model):
	ip_address = models.GenericIPAddressField(unique=True)

	def __str__(self):
		return self.ip_address

class SuspiciousIP(models.Model):
	ip_address = models.GenericIPAddressField()
	reason = models.CharField(max_length=255)
	flagged_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.ip_address} - {self.reason}"

