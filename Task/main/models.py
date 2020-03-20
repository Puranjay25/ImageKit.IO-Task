from django.db import models

# Create your models here.
class UserDetail(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, primary_key=True)
	password = models.CharField(max_length=30)
	ip_address = models.TextField()
	date_created = models.DateField() #YYYY-MM-DD format

	def __str__(self):
		return self.email