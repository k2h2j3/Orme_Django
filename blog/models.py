from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True) # Post테이블이 새로 생성될때의 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정될때마다 시간업데이트

class Comment(models.Model):
    content = models.TextField()
    writer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)