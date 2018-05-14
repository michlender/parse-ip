from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .parseIP import parse_ip

def parseip_page(request):
    return render(request, 'parseip_page/parseip_page.html', {})

@csrf_exempt
def parse(request):
    parsedIPs = parse_ip(request.POST.get('data'))
    return HttpResponse(parsedIPs)
