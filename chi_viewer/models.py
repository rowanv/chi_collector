from django.db import models

class Posting(models.Model):
	title = models.CharField(max_length=300)
	source = models.CharField(max_length=300)
	summary = models.TextField()
	score = models.PositiveIntegerField()
	link = models.CharField(max_length=300)

	date_written = models.DateTimeField()
	will_apply = models.BooleanField(default=False)
	applied = models.BooleanField(default=False)

	def __str__(self):
		return self.title