import imp
from pathlib import Path
from django.http import HttpResponse
import django.shortcuts as Response

def test(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    return HttpResponse('localdb/templates')

def test1(request):
    return Response.render(request, 'test.html', {})
