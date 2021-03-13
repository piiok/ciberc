from django.db import models
from .utils import upload_file_name


class Inventory(models.Model):
    serial_number = models.CharField(max_length=15, unique=True)
    cant = models.CharField(max_length=7)
    price = models.CharField(max_length=10)


class UploadFile(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    file_path = models.FileField(upload_to=upload_file_name)
