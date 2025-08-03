from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    candidate_choice =[
        ('C1', 'candidate1'),
        ('C2', 'candidate2'),
        ('C3', 'candidate3'),
        ('C4', 'candidate4'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_voted = models.BooleanField(default=False)
    candidates = models.CharField(max_length=2, default=None, null=True, blank=True, choices=candidate_choice)

    def __str__(self):
        return f'{self.user.username}-{self.candidates}' 