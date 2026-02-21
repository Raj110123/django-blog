from django.db import models

# Create your models here.

class About(models.Model):
    about_heading=models.CharField(max_length=200)
    about_description=models.TextField(max_length=2000)




    class Meta:
        verbose_name_plural='About'

    
    
    def __str__(self):
        return self.about_heading
    



class SocialLink(models.Model):
    platform=models.CharField(max_length=100)
    link=models.URLField(max_length=200)

    def __str__(self):
        return self.platform


    

