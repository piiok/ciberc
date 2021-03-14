from django.db import models
from .utils import upload_file_name, validate_file, get_summary


class Inventory(models.Model):
    serial_number = models.CharField(max_length=15, unique=True)
    cant = models.CharField(max_length=7)
    price = models.CharField(max_length=10)


class UploadFile(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    file_path = models.FileField(
        upload_to=upload_file_name,
        validators=[validate_file],
    )

    # The maximum number of rows in an excel is 1'048.576
    cant_rows = models.CharField(max_length=6, editable=False)
    cant_products = models.CharField(max_length=15, editable=False)
    average_price_products = models.CharField(max_length=18, editable=False)

    def save_inventory(self, serial_number, cant, price):
        (inventory, created) = Inventory.objects.update_or_create(
            serial_number=serial_number,
            defaults={'cant': cant, 'price': price}
        )

    def save(self, *arg, **kwargs):
        [cant_rows, total_cant, average] = get_summary(
            self.file_path, self.save_inventory)
        self.cant_rows = cant_rows
        self.cant_products = total_cant
        self.average_price_products = average
        super().save()
