from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def parseip_page(request):
    return render(request, 'parseip_page/parseip_page.html', {})

@csrf_exempt
def parse(request):
    # may have to convert request from json to dict? check
    # process (don't worry about this yet)
    # convert result back to json (this you will have to do, Django has machinery to handle returning json?)
    parsedIPs = "done"
    return HttpResponse(parsedIPs)
