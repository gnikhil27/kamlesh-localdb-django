import os
from pathlib import Path
import django.http as http
import django.shortcuts as Response
from . import website
from django.shortcuts import redirect

def test(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    return http.HttpResponse('localdb/templates')

def test1(request):
    return Response.render(request, 'test.html', {})

def main(request,**kwargs):
    userid = request.session.get('mob', None)
    current_page = int(kwargs.get('page') or '1')
    if userid:
        [data_list , last_page] = website.get_data(userid,current_page)
        active_page = request.session.get('page', 'home')
        return Response.render(request, active_page+'.html',{"mob":userid,"data_list":data_list,"last_page":last_page,"current_page":current_page})
    else:
        return Response.render(request, 'login.html', None)


def doLogin(request:http.HttpRequest):
    logout = request.GET.get('logout', 'None')
    if logout == 'true':
        print('Logging Out')
        del request.session['mob']
        return redirect('/main') 
    mobile_no = request.POST.get('mob', None)
    password = request.POST.get('passwd', None)
    if mobile_no and password:
        if website.init_user(mobile_no, password) == 0:
            request.session['mob'] = mobile_no
            return Response.render(request, 'home.html', dict(request.session))
        else:
            return redirect('/main') 
    else:
        return redirect('/main') 

def save_imgs(request):
    website.save_imgs(request)
    return http.HttpResponse('Adding the Images')