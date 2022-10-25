from django.shortcuts import render
from .models import Fitnessgraph
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import Fitnessform
from django.contrib import messages

from blog.forms import Fitnessform


class Fitnessgraph(ListView):
    queryset = Fitnessgraph.objects.all()
    context_object_name = 'Fitnessgraph'
    template_name = 'blog/Fitnessgraph.html'
    model = Fitnessgraph

class Fitnessform(FormView):
    template_name = 'blog/Fitnessform.html'
    form_class = Fitnessform
    success_url = 'blog/Firtstgraph.html'  # リダイレクト先URL

    def form_valid(self, form):
        form.save()  # 保存処理など
        messages.add_message(self.request, messages.SUCCESS, '登録しました！')  # メッセージ出力
        return super().form_valid(form)
