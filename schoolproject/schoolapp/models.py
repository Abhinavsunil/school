from django.db import models

# Create your models here.

class login (models.Model):
    username=models.CharField(max_length=250)
    password=models.IntegerField()
    def __str__(self):
        return self.username

class register(models.Model):
    user_name=models.CharField(max_length=250)
    pass_word=models.IntegerField()
    confirm_pass=models.IntegerField()
    def __str__(self):
        return self.user_name

