from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        view= views.Formulario.as_view(),
        name='formulario_ai',
    ),
    path(
        'ok/',
        view= views.ProcessData.as_view(),
        name='process_data',
    ),

    path(
        'result/',
        view= views.ShowData.as_view(),
        name='show_data',
    ),
    path(
        'cnn/',
        view= views.CNN.as_view(),
        name='cnn',
    ),
    path(
        'rf/',
        view= views.RF.as_view(),
        name='rf',
    )
]
