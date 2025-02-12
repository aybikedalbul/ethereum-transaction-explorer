from django.db import models

class Transactions(models.Model):
    tx_hash = models.CharField(max_length=100, unique=True) 
    from_address = models.CharField(max_length=100) 
    to_address = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=20, decimal_places=10) 
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tx_hash