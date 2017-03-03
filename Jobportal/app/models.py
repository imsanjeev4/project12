from django.db import models

class Register(models.Model):

    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    emailid = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
	
    def __str__(self):
        return self.username
    def __str__(self):
        return self.password

    class Meta:
        db_table = "registered_users"
		
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
	
    def __str__(self):
        return self.description
		
    class Meta:
        db_table = "upload_data"
# Create your models here.
