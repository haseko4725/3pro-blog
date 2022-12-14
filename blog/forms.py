from .models import *
from django import forms


class Fitnessform(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = Fitnessgraph

        #②表示するモデルクラスのフィールドを定義
        fields = ('active','time','day')

        #③表示ラベルを定義
        labels = {'active':"運動名",
                  'time':"時間",
                  'day':"日付",
        }
