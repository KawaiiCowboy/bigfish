from datetime import time
from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=200, help_text="Please write a brief description")
    date = models.DateField(help_text="mm/dd/yyyy")
    description = models.TextField(help_text="Please add a detailed description of your issue.")
    