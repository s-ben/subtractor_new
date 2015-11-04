from django.db import models


class User(models.Model):
    #user_id = models.IntegerField() # Not needed as Django does automatically

	wait_time = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	line_pos = models.IntegerField(null=True)
	

class Audio(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField() 
    # filename = models.CharField(max_length=128)
     # by default uploads to MEDIA_ROOT path in settings.py
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class Document(models.Model):
    docfile = models.FileField()
#     docfile = models.FileField(upload_to='documents/%Y/%m/%d')

