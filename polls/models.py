from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # テキスト数を定義するフィールド
    pub_date = models.DateTimeField('date published') # 日時フィールド
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):# 最も新しい投稿にTureを返す
        # 昨日以降に作成された投稿にTureを返す
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #リレーションシップ定義 
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0) # 数字を定義するフィールド
    def __str__(self):
        return self.choice_text
