from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')


class PersonDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_id')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(User, UserAdmin)
admin.site.register(UserType)
admin.site.register(EntityUser)
admin.site.register(PersonDetails, PersonDetailsAdmin)
admin.site.register(PersonAddress)
admin.site.register(Industry)
admin.site.register(ParentEntityName)
admin.site.register(Entity)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(OrderItems)