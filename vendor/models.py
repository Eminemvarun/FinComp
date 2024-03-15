from django.db import models

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
  
  def __str__(self):
      return self.company_name
    