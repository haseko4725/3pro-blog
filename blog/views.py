from django.views.generic import TemplateView
from . import models
from . import graph


class Index(TemplateView):

    #テンプレートファイル連携
    template_name = "Fitnessgraph.html"

    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):

        #グラフオブジェクト
        qs    = models.ProductA.objects.all()  #モデルクラス(ProductAテーブル)読込
        x     = [x.Date for x in qs]           #X軸データ
        y     = [y.Revenue for y in qs]        #Y軸データ
        chart = graph.Plot_Graph(x,y)          #グラフ作成

        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
        return context

    #get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)