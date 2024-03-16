from django.db import models
class Logger(models.Model): 
    
    name = models.CharField( max_length=50) 
    address = models.CharField( max_length=100) 
    email=models.EmailField()
    
def _str_(self):
    return self.name