from django.db import models

# Create your models here.
class Sector(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['id']
        verbose_name_plural = "Sectors"
    
    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete= models.SET_NULL, null= True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"
        
    
    def __str__(self):
        return f"{self.name}-{self.sector}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="No Description")
    price = models.IntegerField(default= 0)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null= True)
    
    
    
    
    