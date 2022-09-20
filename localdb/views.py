import os
from pathlib import Path
import django.http as http
import django.shortcuts as Response
from . import website

def test(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    return http.HttpResponse('localdb/templates')

def test1(request):
    return Response.render(request, 'test.html', {})

def main(request):
    userid = request.session.get('mob', None)
    if userid:
        current_page = request.session.get('page', 'home')
        return Response.render(request, current_page+'.html')
    else:
        return Response.render(request, 'login.html', None)


def doLogin(request:http.HttpRequest):
    logout = request.GET.get('logout', 'None')
    if logout == 'true':
        print('Logging Out')
        del request.session['mob']
        return main(request)
    mobile_no = request.POST.get('mob', None)
    password = request.POST.get('passwd', None)
    if mobile_no and password:
        if website.init_user(mobile_no, password) == 0:
            request.session['mob'] = mobile_no
            return Response.render(request, 'home.html', dict(request.session))
        else:
            return main(request)
    else:
        return main(request)

def save_imgs(request):
    website.save_imgs(request)
    return http.HttpResponse('Adding the Images')