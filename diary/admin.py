from django.contrib import admin
from .models import Page

# ModelAdmin を継承して PageAdmin を定義
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    # 読み取り専用フィールドを設定
    readonly_fields = ["id", "created_at", "updated_at"]
