from django.db import models

class Userdata(models.Model):
    fname = models.CharField(max_length=50,verbose_name="first name")
    lname = models.CharField(max_length=50,verbose_name="last name")
    email = models.EmailField(verbose_name='userEmail')
    review = models.TextField(verbose_name="User review")
    

    def __str__(self):
        return self.fname

   

    
    
