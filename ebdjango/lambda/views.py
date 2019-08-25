from django.shortcuts import render
from django.views import View
# Create your views here.
import telebot
import requests
import s3io
import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.oauth2 import service_account

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

    DIALOGFLOW_PROJECT_ID = 'newagent-mdwbir'
    DIALOGFLOW_LANGUAGE_CODE = 'es'
    GOOGLE_APPLICATION_CREDENTIALS = './config/newagent-mdwbir-bde964affdea.json'
    SESSION_ID = 'current-user-id'

    @csrf_exempt    
    def post(self,request):

        credentials = service_account.Credentials.from_service_account_file(self.GOOGLE_APPLICATION_CREDENTIALS)
        session_client = dialogflow.SessionsClient(credentials=credentials)

        session = session_client.session_path(self.DIALOGFLOW_PROJECT_ID, self.SESSION_ID)

        text_input = dialogflow.types.TextInput(text=request.POST["message"], language_code=self.DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)

        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
            raise
        print(response.query_result.fulfillment_text)

        ctx = {
            "dialog": response.query_result.fulfillment_text
        }
        print(ctx)
        return JsonResponse(ctx)

    def get(self,request):
        
        return  HttpResponse(hub_challenge)
    """
    def get_dialog_response(self,request):
        bucket = "meer-models"
        key="knn.sav"
        
        
        with s3io.open('s3://{0}/{1}'.format(bucket, key), mode='r',
            **credentials) as s3_file:
            knn = joblib.load(s3_file)
        return HttpResponse("ok")

        return  HttpResponse(hub_challenge)
    """ 


