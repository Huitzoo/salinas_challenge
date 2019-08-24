from django.shortcuts import render


class Analisis(View):

    def post(self,request):
        
        datos_medicos = forms.DatosMedicosForm(request.POST)
        return render(request,"dashboard.html")
    
    def get(self,request):

        return render(request,"formulario.html",response)

