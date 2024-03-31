from django.db import models

# Create your models here.
class Bills(models.Model):
    bill_name=models.CharField(max_length=100)
    due_date=models.DateField(null=True, blank=True)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.BooleanField(default=False)
