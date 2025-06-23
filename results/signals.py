from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Result


@receiver(pre_save, sender=Result)
def total_scores(sender, instance, **kwargs):
    if not instance:
        instance.total = 0
        instance.grade = ''
    else:
        instance.total=(instance.project_score + instance.note_score + instance.ass_score + ca_score + instance.exam_score)
    
    if 90 <= instance.total <= 100:
        instance.grade = 'A'
    elif 80 <= instance.total <= 89:
        instance.grade = 'B'
    elif 70 <= instance.total <= 79:
        instance.grade = 'C'
    elif 60 <= instance.total <= 69:
        instance.grade = 'D'
    elif 45 <= instance.total <= 59:
        instance.grade = 'E'
    else:
        instance.grade = 'F'
    


