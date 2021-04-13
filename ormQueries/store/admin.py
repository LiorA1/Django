from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Contact)
admin.site.register(models.Customer)
admin.site.register(models.Employee)
admin.site.register(models.Department)
admin.site.register(models.FinCode)
admin.site.register(models.FinData)
admin.site.register(models.Product)
admin.site.register(models.SalesOrder)
admin.site.register(models.SalesOrderItems)
