from django.db import models

# Create your models here.
class list(models.Model):
	item=models.CharField(max_length=200)
	completed=models.BooleanField(default=False)
	time = models.TimeField(null=True)

	def __str__(self):
		return self.item + ' | ' + str(self.completed)