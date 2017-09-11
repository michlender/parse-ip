from django.shortcuts import render

def parseip_page(request):
    return render(request, 'parseip_page/parseip_page.html', {})
