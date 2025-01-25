import os

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser


# Create your views here.

def login(request):
    return HttpResponse("登录页面")


@action(methods=['post'], detail=True)
def start_record(request):
    request_body = JSONParser().parse(request)
    filename = request_body['name']

    cmd = "nohup ffmpeg  -video_size $(xdpyinfo | grep 'dimensions:'|awk '{print $2}') -f x11grab -draw_mouse 1 -i :0.0+0,0 -vf 'scale=trunc(iw/2)*2:trunc(ih/2)*2' -r 60.0 -profile:v  high444 -level 4.1 -pix_fmt yuv420p -preset:v ultrafast /mnt/hgfs/devWorkspace/record_demo/output.mp4 -y >> /mnt/hgfs/devWorkspace/record_demo/ffmpeg_record.log 2>&1 &"

    print(cmd)

    os.system(cmd)

    output = os.popen("ps ax | grep ffmpeg")
    aa = output.read()
    print(aa)

    print(filename)
