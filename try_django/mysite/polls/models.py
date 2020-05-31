import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    #models.Model이라는 class상속받는거 근데 안보여!
    question_text = models.CharField(max_length=200)
    #char저것도 클래스 이름중하나래
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #foreignkey라는건 다른 table에있는 key를 가져온다고 하는것 question의 키 가져옴
    choice_text = models.CharField(max_length=200)
    #선택지 생성
    votes = models.IntegerField(default=0)
    #누가 몇표를 찍었나 알려주는거
    
    def __str__(self):
        return self.choice_text