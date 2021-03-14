from django.contrib import admin
from django.utils.html import format_html
from .models import Inventory, UploadFile
import json


class UploadFileAdmin(admin.ModelAdmin):
    readonly_fields = ('summary', 'json_data')
    list_display = ('name', 'summary', 'excel_file', 'created_date')

    def json_data(self, obj):
        json_data = {
            "elements": int(obj.cant_rows),
            "precio promedio": float(obj.average_price_products),
        }

        return json.dumps(json_data)

    def excel_file(self, obj):
        template = f'''
          <a href="/{obj.file_path}" download>
            {obj.file_path}
          </a>
        '''
        return format_html(template)

    def summary(self, obj):
        template = f'''
          <b>Cant rows:</b> {obj.cant_rows} <br/>
          <b>Cant products:</b> {obj.cant_products} <br/>
          <b>Average prices products:</b> $ {obj.average_price_products} <br/>
        '''
        return format_html(template)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'cant', 'price_formmat')

    def price_formmat(self, obj):
        template = f' <b>$</b> {obj.price}'
        return format_html(template)
    price_formmat.short_description = "PRICE"


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(UploadFile, UploadFileAdmin)
