from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.team_name}'

    class Meta:
        verbose_name_plural = 'Teams'


class Members(models.Model):
    name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Members'


class HappinessLevel(models.Model):
    CHOICES = (
        (1, 'Joy'),
        (2, 'Excitement'),
        (3, 'Gratitude'),
        (4, 'Pride'),
        (5, 'Optimism'),
        (6, 'Contentment'),
        (7, 'Love')
    )
    level = models.IntegerField(choices=CHOICES)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_level_display()

    class Meta:
        verbose_name_plural = 'HappinessLevel'

