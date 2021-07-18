from django.db import models

from datetime import datetime

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    title = models.CharField(max_length=2)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)

    class Meta:
        # managed = False
        db_table = 'contact'


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=20)
    address = models.CharField(max_length=35)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    company_name = models.CharField(max_length=35)

    class Meta:
        # managed = False
        db_table = 'customer'


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    manager = models.ForeignKey("Employee", on_delete=models.PROTECT, null=True) # ForeignKey
    emp_fname = models.CharField(max_length=20)
    emp_lname = models.CharField(max_length=20)
    # dept_id = models.OneToOneField("Department", on_delete=models.PROTECT) ## ForeignKey
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=4)
    zip_code = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=1)
    ss_number = models.CharField(max_length=11)
    salary = models.FloatField(max_length=20)  # This field type is a guess.
    start_date = models.DateField(default=datetime.now)
    termination_date = models.DateField(null=True)
    birth_date = models.DateField(default=datetime.now)
    bene_health_ins = models.CharField(max_length=1)
    bene_life_ins = models.CharField(max_length=1)
    bene_day_care = models.CharField(max_length=1)
    sex = models.CharField(max_length=1)

    class Meta:
        # managed = False
        db_table = 'employee'


class EmpToDep(models.Model):
    departmentKey = models.ForeignKey("Department", on_delete=models.PROTECT)  ## foreignkey
    employeeKey = models.ForeignKey("Employee", on_delete=models.PROTECT)  ## foreignkey
    start_date = models.DateField(default=datetime.now)
    termination_date = models.DateField(null=True)
    ismanager = models.BooleanField(default=False)


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=40)
    # dept_head_id = models.OneToOneField(Employee, on_delete=models.PROTECT) # ForeignKey

    class Meta:
        # managed = False
        db_table = 'department'


class FinCode(models.Model):
    code = models.CharField(primary_key=True, max_length=2)
    typeOf = models.CharField(max_length=10)
    description = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'fin_code'


class FinData(models.Model):
    year = models.CharField(max_length=4)
    quarter = models.CharField(max_length=2)
    code = models.ForeignKey(FinCode, on_delete=models.PROTECT)
    amount = models.FloatField(max_length=9)  # This field type is a guess.

    class Meta:
        # managed = False
        constraints = [models.UniqueConstraint(fields=['year', 'quarter', 'code'], name='fin_data_pk')]
        db_table = 'fin_data'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=30)
    size = models.CharField(max_length=18)
    color = models.CharField(max_length=6)
    quantity = models.IntegerField()
    unit_price = models.FloatField(max_length=15)  # This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'product'


class SalesOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_date = models.DateField()
    fin_code = models.ForeignKey(FinCode, on_delete=models.PROTECT)
    region = models.CharField(max_length=7)
    sales_rep = models.ForeignKey(Employee, on_delete=models.PROTECT)

    class Meta:
        # managed = False
        db_table = 'sales_order'


class SalesOrderItems(models.Model):
    sale_order = models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
    line_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    ship_date = models.DateField()

    class Meta:
        # managed = False
        constraints = [models.UniqueConstraint(fields=['sale_order', 'line_id'], name='sales_order_items_pk')]
        db_table = 'sales_order_items'
