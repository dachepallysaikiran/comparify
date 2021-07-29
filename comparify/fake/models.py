from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    rating=models.DecimalField(decimal_places=1,max_digits=2, default=0)
    desc=models.CharField(max_length=300, default='none')
    source=models.CharField(max_length=300, default='none')
    url=models.CharField(max_length=1000, default='none')
    image= models.ImageField(upload_to="fake/images",default="")
    def __str__(self):
        return self.product_name