from django import forms

class Fitnessform(forms.Form):
    active = forms.fields.ChoiceField(
        choices = (
            ('',''),
            (3.0, 'バレーボール'),
            (3.5, 'ゴルフ'),
            (4.0, '卓球'),
            (4.5, 'バドミントン'),
            (5.0, '野球'),
            (6.0, 'バスケットボール'),
            (7.0, 'サッカー'),
            (8.0, 'ランニング'),
        ),
        initial=10,
        required=True,
        widget=forms.widgets.Select()
    )

    time = forms.IntegerField(label="時間")
    day = forms.TimeField("日付")

