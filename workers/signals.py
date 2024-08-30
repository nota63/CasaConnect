from urllib import request

from django.db.models.signals import post_save
from django.dispatch import receiver


from .models import Complaint


@receiver(post_save, sender=Complaint)
def complaint_post_save(sender, instance, created, **kwargs):
    print('------New Complaint created successfully----')
    print('Sender:',sender)
    print('Instance:',instance)
    print('created:',created)
    print(f'**Kwargs: {kwargs}')

