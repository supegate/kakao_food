from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['1', '2' ]
        })

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']

    return JsonResponse({
        'message': {
            'text': "Hello "+return_str+"!\nThis is test app.\n한글 안녕하세요.",
            'photo': {
               #  'url': "https://dummyimage.com/640x480/eb00eb/fff",
                 'url': "http://218.237.81.19:9000/static/images1.jpeg",
                 'width': 277,
                 'height': 182
             },
             'message_button': {
                 'label': "라벨입니다.",
                 'url': "http://218.237.81.19:9001"
             }  
         },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['1', '2']
         }
    })


