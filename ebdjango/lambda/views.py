from django.shortcuts import render
from django.views import View
# Create your views here.
import telebot
import requests
import s3io

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class Messenger(View):
    TELEGRAM_URL = "https://api.telegram.org/bot"
    BOT_TOKEN = "956441882:AAEcXMjJXJlogNVoDJ1MLuXwuQJ8ds_rbfg"
    CHAT_ID = "895357693"
    @csrf_exempt    
    def post(self,request):
    
        data = {
            "chat_id": self.CHAT_ID,
            "text": "ahhhhhhhhh"
        }
        response = requests.post(self.TELEGRAM_URL+self.BOT_TOKEN+"/sendMessage", data=data)

        
        return HttpResponse("ok")
    
    def get(self,request):
        
        return  HttpResponse(hub_challenge)


class Dialog(View):
    @csrf_exempt    
    def post(self,request):
        print(request)
        
        
        return HttpResponse("ok")
    
    def get(self,request):
        
        return  HttpResponse(hub_challenge)


class Web(View):
    credentials_amazon = dict(
        aws_access_key_id="AKIATAIHD3W7Z3XTQJEV",
        aws_secret_access_key="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",
    )
    @csrf_exempt    
    def post(self,request):
        print(request.POST["message"])
        bucket = "meer-models"
        key="knn.sav"
        
        with s3io.open('s3://{0}/{1}'.format(bucket, key), mode='r',
            **credentials) as s3_file:
            knn = joblib.load(s3_file)
        return HttpResponse("ok")
    
    def get(self,request):
        
        return  HttpResponse(hub_challenge)

    def get_dialog_response(self,request):
        
        return  HttpResponse(hub_challenge)



