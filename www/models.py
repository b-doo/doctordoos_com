from django.db import models
from mezzanine.core.fields import RichTextField

# Create your models here.

class DDLPFeedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feedback = models.TextField()


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()