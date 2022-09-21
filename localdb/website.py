from django.shortcuts import render
from PIL import Image
import os, json
from io import BytesIO
import base64

def init_user(mob, passwd):
    if not os.path.exists("data/"+mob):
        os.makedirs("data/"+mob)
    user_file = "data/"+mob+"/info.json"
    if os.path.exists(user_file):
        user_data = json.load(open(user_file))
        if user_data['password'] == passwd:
            return 0
        else:
            return 1
    else:
        user_data = {"password":passwd}
        json.dump(user_data, open(user_file, 'w'))
        return 0


def save_imgs(request):
    if request.session['mob']:
        file = request.FILES['imgs']
        print('---------------', base64.encodebytes(file.read()))
        return 0

