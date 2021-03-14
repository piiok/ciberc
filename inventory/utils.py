import os
from uuid import uuid4
from django.core.exceptions import ValidationError

from pyxlsb import open_workbook


def upload_file_name(instance, filename):
    path = 'uploads/upload_file'
    if(instance.id):
        return f'{path}/{instance.id}_{filename}'
    else:
        return f'{path}/{uuid4().hex}_{filename}'


def validate_file(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xlsb']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def get_summary(file_field, save_inventary):
    total_cant = 0
    total_price = 0
    cant_rows = 0
    with open_workbook(file_field) as wb:
        with wb.get_sheet(1) as sheet:
            for row in sheet.rows():
                serial_name = row[0][2]
                cant = row[1][2]
                price = row[2][2]
                if(serial_name is not None and cant is not None and price is not None):
                    save_inventary(int(serial_name), int(cant), int(price))
                    cant_rows += 1
                    total_cant += cant
                    total_price += price
                else:
                    break
    average = total_price/cant_rows
    return [cant_rows, int(total_cant), average]
