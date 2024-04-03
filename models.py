from django.db import models
from django.contrib.auth.models import User

class Kids(models.Model):
    Book_Name = models.CharField(max_length = 500)
    Book_Aurthor = models.CharField(max_length = 500)
    Book_Type = models.CharField(max_length = 500)
    Book_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  
    Book_Description = models.TextField(default='NA')
    Book_Image=models.ImageField(upload_to='book_image',default='NA')

class Sci_Fyi(models.Model):
    Book_Name = models.CharField(max_length = 500)
    Book_Aurthor = models.CharField(max_length = 500)
    Book_Type = models.CharField(max_length = 500)
    Book_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)   # Add new field for book price
    Book_Description = models.TextField(default='NA')
    Book_Image=models.ImageField(upload_to='book_image1',default='NA')

class Love(models.Model):
    Book_Name = models.CharField(max_length = 500)
    Book_Aurthor = models.CharField(max_length = 500)
    Book_Type = models.CharField(max_length = 500)
    Book_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)   # Add new field for book price
    Book_Description = models.TextField(default='NA')
    Book_Image=models.ImageField(upload_to='book_image2',default='NA')
class Story(models.Model):
    Book_Name = models.CharField(max_length = 500)
    Book_Aurthor = models.CharField(max_length = 500)
    Book_Type = models.CharField(max_length = 500)
    Book_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)   # Add new field for book price
    Book_Description = models.TextField(default='NA')
    Book_Image=models.ImageField(upload_to='book_image3',default='NA')

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Kids, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class CartItemL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Love, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class CartItemS(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Sci_Fyi, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class CartItemT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Story, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Customer(models.Model):
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # we have created Many-to-one relationship i.e multiple order can be done by one user
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    pincode = models.IntegerField(
        default=0,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return str(self.id)
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Kids = models.ForeignKey(Kids, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return str(self.id)
    
class Order1(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Love = models.ForeignKey(Love, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return str(self.id)
    
class Order2(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Sci_Fyi = models.ForeignKey(Sci_Fyi, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return str(self.id)
    
class Order3(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Story = models.ForeignKey(Story, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return str(self.id)

# Create your models here.
