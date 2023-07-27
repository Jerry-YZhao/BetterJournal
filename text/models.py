from django.db import models

class Goal(models.Model):
    goal_name = models.CharField(max_length=255)

class Progress(models.Model):
    date = models.DateField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    progress_value = models.IntegerField()