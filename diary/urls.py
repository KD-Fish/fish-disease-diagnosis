from django.urls import path
from . import views

# アプリ名
app_name = "diary"

# URLパターンリスト
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.PageCreateView.as_view(), name="page_create"),
    path("pages/",views.page_list,name="page_list"),
    #uuidには日記のidが入る
    path("page/<uuid:id>",views.page_detail,name="page_detail"),
    path("page/<uuid:id>/update/",views.page_update,name="page_update"),
    path("page/<uuid:id>/delete/",views.page_delete,name="page_delete")

]
