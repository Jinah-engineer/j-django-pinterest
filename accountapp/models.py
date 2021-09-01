from django.db import models

# python managepy makemigrations -- models.py 에 쓰는 내용을 DB와 연동시킬 python file 로 만들어주는 작업
# python manage.py migrate -- migration 적용


class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)