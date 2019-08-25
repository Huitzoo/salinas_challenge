from django.urls import path
from . import views

urlpatterns = [
    path(
        '/dialog',
        view= views.Dialog.as_view(),
        name='dialog',
    ),
    path(
        '/web',
        view= views.Web.as_view(),
        name='web-bot',
    ),

]