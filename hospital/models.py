from django.db import models

# Create your models
class appointment(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=500)
    select_Date=models.DateField()
    select_Department=models.CharField(max_length=50)
    Phone_Number=models.IntegerField()
    Additional_Message=models.TextField()

    def __str__(self):
        return self.Name




