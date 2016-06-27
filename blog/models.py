from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User') # ForeignKey : 다른 모델에 대한 링크를 의미
    title = models.CharField(max_length=200)    # CharField : 글자 수가 제한된 텍스트를 정의할 때 사용.
    text = models.TextField()   # TextField: 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(default=timezone.now)   # DateTimeField: 날짜와 시간을 의미

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
