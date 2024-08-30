from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# create help model

class HelpMod(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.EmailField()
    contact=models.CharField(max_length=100)
    keywords=models.CharField(max_length=10000, null=True)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.user} - {self.contact}'
