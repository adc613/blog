from django.db import models

# Create your models here.
class Debate(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Argument(models.Model):
    argument = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey('accounts.User')
    dabte_thread = models.ForeignKey(Debate)

    def __str__(self):
        return self.debate.title + ': ' + self.creation_date + ', ' + str(self.creator)
