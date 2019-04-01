from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("For support please contact us at cnfa.org")


def contact(request):
    return HttpResponse("For support please contact us at cnfa.org")


def logo(request):
    template_url = 'logo.html'
    return render(request, template_url)
