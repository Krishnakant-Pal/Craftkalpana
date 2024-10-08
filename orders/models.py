from django.db import models
from accounts.models import Account
from store.models import Product


class Payment(models.Model):
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id      = models.CharField(max_length=100)
    payment_method  = models.CharField(max_length=100)
    amount_paid     = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount paid
    status          = models.CharField(max_length=100)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    user         = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment      = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    phone        = models.CharField(max_length=15)
    pincode      = models.IntegerField()
    email        = models.EmailField(max_length=50)
    address      = models.CharField(max_length=200)
    city         = models.CharField(max_length=50)
    state        = models.CharField(max_length=50)
    order_total  = models.DecimalField(max_digits=10, decimal_places=2)
    gst          = models.DecimalField(max_digits=10, decimal_places=2)
    status       = models.CharField(max_length=10, choices=STATUS, default='New')
    ip           = models.CharField(max_length=20, blank=True, null=True)
    is_ordered   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)


    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.order_number


class OrderProduct(models.Model):
    order         = models.ForeignKey(Order,  on_delete=models.CASCADE)
    user          = models.ForeignKey(Account, on_delete=models.CASCADE)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment       = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    quantity      = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered       = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name