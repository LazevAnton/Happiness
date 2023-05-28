from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.team_name}'


class Members(models.Model):
    name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.last_name}'
