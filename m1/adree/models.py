from django.db import models

# Create your models here.
class SignUp(models.Model):
    userid=models.PositiveSmallIntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    birthdate = models.DateField(help_text = "your birthdate" )
    email=models.EmailField()
    gender=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    password=models.CharField(max_length=32)

    def __str__(self): 
        return self.name