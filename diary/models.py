from django.db import models
from pathlib import Path #削除機能を実行時フォルダから画像を削除するため
import uuid

# データのテーブルに該当するクラスを定義
class Page(models.Model):
    # IDカラム(UUIDから取得)で、デフォルト値としてIDを格納し、編集不可能にする
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    
    # タイトルを最大100文字まで設定
    title = models.CharField(max_length=100, verbose_name="タイトル")
    
    # 本文を格納する変数
    body = models.TextField(verbose_name="本文")
    
    # 日付を取得して格納する変数
    page_date = models.DateField(verbose_name="日付")
    
    #画像保存先を指定して画像を格納する変数
    picture = models.ImageField(upload_to="diary/picture/", blank=True, null=True, verbose_name="写真")
    
    # 作成日時を一度のみ自動で取得
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    
    # 更新日時を毎回更新
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    def __str__(self):
        return self.title
    
    #可変長のデータをタプルで受け取る
    def delete(self, *args, **kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        #もし画像があるのであれば削除
        if picture:
            Path(picture.path).unlink(missing_ok=True)

