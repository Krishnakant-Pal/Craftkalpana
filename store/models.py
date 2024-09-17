from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg,Count
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
    
    def review_average(self):
        reviews = Reviews.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def review_average_percent(self):
        reviews = Reviews.objects.filter(product=self, status=True).aggregate(average=Avg('rating')) or 0
        per = 0
        if reviews['average'] is not None:
            per = (reviews['average'] * 100 )/ 5
        return per

    def review_count(self):
        reviews = Reviews.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    def __str__(self):
        return self.subject