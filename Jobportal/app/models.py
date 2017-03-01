from django.db import models

class Register(models.Model):

    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    emailid = models.CharField(max_length=30)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.username

    class Meta:
        db_table = "registered_users"
# Create your models here.
