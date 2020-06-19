from django.db import models

# Create your models here.
class Uploadmyfiles(models.Model):
    upload_file = models.FileField(upload_to ='profiles')
    upload_date = models.DateTimeField(auto_now_add =True)
