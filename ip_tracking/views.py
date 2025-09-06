# Views for IP Tracking
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit

def home_view(request):
    return HttpResponse("Welcome to the IP Tracking App!")

@csrf_exempt
@ratelimit(key='ip', rate='10/m', method='POST', block=True)
@ratelimit(key='ip', rate='5/m', method='POST', block=True, group='anonymous')
def login_view(request):
    if request.method == 'POST':
        return HttpResponse('Login attempt')
    return HttpResponse('Login page')

