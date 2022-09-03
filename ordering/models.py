from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status_order_id = models.ForeignKey('StatusOrder', null=True, on_delete=models.PROTECT)
    type_work = models.CharField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    name_work = models.CharField(max_length=100, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    cost_work = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    file_order = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.type_work} - {self.subject} - {self.name_work}'


class StatusOrder(models.Model):
    status = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.status}'
