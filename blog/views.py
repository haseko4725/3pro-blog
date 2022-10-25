from django.shortcuts import render
from .models import Fitnessgraph
from django.views.generic import ListView
from django.views.generic import TemplateView
from . import forms


class Fitnessgraph(ListView):
    queryset = Fitnessgraph.objects.all()
    context_object_name = 'Fitnessgraph'
    template_name = 'blog/Fitnessgraph.html'
    model = Fitnessgraph

class Fitnessform(TemplateView):

    # 初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "Fitnessform":forms.Contact_Form(),
                       }

    # GET時の処理を記載
    def get(self,request):
        return render(request, "blog/Fitnessform.html",context=self.params)

    # POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["Fitnessform"] = forms.Contact_Form(request.POST)
            
            # フォーム入力が有効な場合
            if self.params["Fitnessform"].is_valid():
                self.params["Message"] = "入力情報が送信されました。"

        return render(request, "blog/Fitnessform.html",context=self.params)
    
