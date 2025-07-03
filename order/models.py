from django.db import models

class Customer(models.Model):
    customerName = models.CharField(max_length=50)
    contactLastName = models.CharField(max_length=50)
    contactFirstName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressLine = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"Name:{self.customerName}, City:{self.city}"

class Product(models.Model):
    productName = models.CharField(max_length=70)
    productScale = models.CharField(max_length=10)
    productDescription = models.TextField()
    quantityInStock = models.SmallIntegerField()
    buyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    MSRP = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.productName

class Order(models.Model):
    orderDate = models.DateTimeField()
    requiredDate = models.DateTimeField()
    status = models.CharField(max_length=15)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantityOrdered = models.IntegerField()
    priceEach = models.DecimalField(max_digits=10, decimal_places=2)
    orderLineNumber = models.SmallIntegerField()

    def __str__(self):
        return f"OrderDetail {self.id} for Order {self.order.id}"