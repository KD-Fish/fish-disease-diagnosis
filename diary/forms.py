from django.forms import ModelForm
from .models import Page

class PageForm(ModelForm):
    class Meta:
        model = Page
        #ユーザーが書き込む要素(タイトルと本文,日時は取得)
        fields = ["title","body","page_date","picture"]