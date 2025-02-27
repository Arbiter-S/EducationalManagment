import random

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=User)
def code(instance, **kwargs):
    if not instance.username:
        code_length = 10
        code = "".join(random.choice("0123456789") for _ in range(code_length))
        if instance.role in ("STU", "PRO", "AST", "ADM") and instance.role is not None:
            username = f"{instance.role}-{code}"
            instance.username = username
            instance.save()


@receiver(pre_save, sender=Student)
def military(sender, instance, **kwargs):
    if instance.user.gender == "M":
        instance.military_status = instance.get_military_status()
    else:
        instance.military_status = None


@receiver(post_save, sender=ITAdmin)
def superuser(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.is_superuser = True
        user.is_staff = True
        user.save()


@receiver(post_save, sender=Student)
def set_academic_term(sender, instance, created, **kwargs):
    if created:
        if instance.degree == "B":
            instance.academic_terms = 8
        elif instance.degree == "M":
            instance.academic_terms = 4
        elif instance.degree == "D":
            instance.academic_terms = 10
        instance.save()
