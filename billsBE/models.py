from django.db import models

# Create your models here.
class Bills(models.Model):
    bill_name=models.CharField(max_length=100)
    due_date=models.DateField(null=True, blank=True)
    amount=models.FloatField()
    status=models.BooleanField(default=False)
