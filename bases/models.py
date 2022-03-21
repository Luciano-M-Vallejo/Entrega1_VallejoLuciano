from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=20)
    subTitle = models.CharField(max_length=20)
    body = models.TextField()
    author = models.CharField(max_length=20)
    date = models.DateTimeField()
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    webLink = models.URLField()
   
    
class Bibliography(models.Model):
    main = models.TextField(max_length=1000)
    author = models.CharField(max_length=20)
    webLink = models.URLField()
    
    def __str__(self):
        return f'''Autor: {self.author} -
                   Link: {self.webLink} - 
                   Bibliografia: {self.main}'''