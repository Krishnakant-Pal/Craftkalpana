from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name        = models.CharField(max_length=200,unique=True)
    slug                = models.SlugField(max_length=200,unique=True)
    description         = models.TextField(max_length=500,blank=True)
    price               = models.DecimalField(max_digits=10, decimal_places=2,default = 0.00)
    images              = models.ImageField(upload_to='photos/products')
    stock               = models.IntegerField()
    is_available        = models.BooleanField(default = True)
    category            = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now_add=True)
    item_type           = models.CharField(max_length=200, default="Not specified")
    Dimensions          = models.CharField(max_length=200, default="Dimensions not available")
    color               = models.CharField(max_length=200,default="Color not specified")
    state_of_origin     = models.CharField(max_length=200,default="Unknown")

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])
    
    def __str__(self):
        return self.product_name
    
