from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    is_staff = models.BooleanField(null=True)
    is_vendor = models.BooleanField(null=True)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField(null=True)


class UserType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EntityUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    entity_id = models.IntegerField(null=True)


class PersonDetails(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email_id = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PersonAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    lat = models.IntegerField(null=True)
    lng = models.IntegerField(null=True)


class Industry(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ParentEntityName(models.Model):
    name = models.CharField(max_length=200, null=True)
    industry_type = models.ManyToManyField(Industry, blank=True, null=True)
    is_disabled = models.BooleanField(null=True)
    description = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)


class Entity(models.Model):
    parent_entity = models.ForeignKey(ParentEntityName, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    is_disabled = models.BooleanField(null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    pincode = models.IntegerField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    is_barcode = models.BooleanField(null=True)
    description = models.CharField(max_length=200, null=True)
    sub_url = models.CharField(max_length=200, null=True)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    buying_price = models.FloatField(null=True)
    list_price = models.FloatField(null=True)
    selling_price = models.FloatField(null=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_disabled = models.BooleanField(null=True)
    discount = models.FloatField(null=True)
    out_off_stock = models.BooleanField(null=True)
    partner_product_id = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    person_id = models.ForeignKey(PersonDetails, null=True, on_delete=models.SET_NULL)
    entity = models.ForeignKey(Entity, null=True, on_delete=models.SET_NULL)
    order_unique_id = models.CharField(max_length=1000, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    booked_ref = models.CharField(max_length=1000, null=True)
    notes = models.CharField(max_length=1000, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateTimeField(auto_now_add=True)
    closed_by = models.ForeignKey(EntityUser, on_delete=models.CASCADE)


class OrderItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    pricelist = models.FloatField(null=True)
    list_price = models.FloatField(null=True)
    selling_price = models.FloatField(null=True)
    buying_price = models.FloatField(null=True)
