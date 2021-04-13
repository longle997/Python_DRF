from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length=100)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question

class Choise(models.Model):
	# The related_name attribute specifies the name of the reverse relation from the Poll model back to your model.
	# For example to refer choise of any poll instance you can use 'Poll.choise.all()'
	# you could use Poll.choise.all() to get all instances of your Choise model that have a relation to current_poll
	poll = models.ForeignKey(Poll, related_name='choise', on_delete=models.CASCADE)
	choise_text = models.CharField(max_length=100)

	def __str__(self):
		return self.choise_text

class Vote(models.Model):
	choise = models.ForeignKey(Choise, related_name='votes', on_delete=models.CASCADE)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

	# if you want to override the default behavior of fields, you can define the corresponding meta options
	class Meta:
		unique_together = ('poll', 'voted_by')