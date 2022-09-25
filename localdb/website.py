from django.shortcuts import render
from PIL import Image
import os, json
from io import BytesIO
import base64
import math

def get_data(mob,offset=1,limit=10):
    offset = offset - 1
    list_of_data = list(map(lambda x : "data/"+mob+"/"+x,filter(lambda x : x.endswith(".jpeg"),os.listdir("static/data/"+mob))))
    last_page = math.ceil(len(list_of_data) / limit)
    return [list_of_data[offset*limit:offset*limit+limit], last_page]

def init_user(mob, passwd):
    if not os.path.exists("static/data/"+mob):
        os.makedirs("static/data/"+mob)
    user_file = "static/data/"+mob+"/info.json"
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
    mob = request.session.get('mob')
    if mob:
        file = request.FILES['imgs']
        if not file:
            return 0   
        if not os.path.exists("static/data/"+mob):
            os.makedirs("static/data/"+mob)
        user_file = "static/data/"+mob+"/info.json"
        if os.path.exists(user_file):
            user_data = json.load(open(user_file))
            img_count = user_data.get('last_img_count') or '0'
            new_file = str(int(img_count)+1)
            img_file = open("static/data/"+mob+'/'+new_file+'.jpeg', 'wb')
            base64_data = base64.encodebytes(file.read())
            img_file.write(base64.decodebytes(base64_data))
            img_file.close()
            user_data['last_img_count'] = new_file
            json.dump(user_data, open(user_file, 'w'))
    return 0