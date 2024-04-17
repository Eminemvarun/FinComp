from django.db import models
from PIL import Image

# Create your models here.

class Vendor(models.Model):
  ref_no = models.IntegerField()
  company_name = models.CharField(max_length=255)
  software_name = models.CharField(max_length=255)
  company_website = models.URLField()
  type_of_software = models.CharField(max_length=255)
  description = models.TextField(max_length=255)
  company_established = models.IntegerField()
  countries = models.CharField(max_length=255) 
  cities  = models.CharField(max_length=255)
  contact_no = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  employees = models.IntegerField()
  professional_services = models.CharField(max_length=255)
  last_demo_date = models.DateField()
  last_reviewed_date = models.DateField()
  image = models.ImageField(default="vendor/static/vendor/default.jpg",upload_to="profile_pics")
  
  
  def __str__(self):
      return self.company_name
  
  def save(self):
     super().save()
     img = Image.open(self.image.path)
     if(img.height>500 or img.width>500):
        output_size = (500,500)
        img.thumbnail(output_size)
        img.save(self.image.path) 