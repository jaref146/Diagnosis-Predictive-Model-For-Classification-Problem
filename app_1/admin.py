from django.contrib import admin

# Register your models here.
from .models import sale_book, contact_info_tabel, wish_list_table

admin.site.register(sale_book),
admin.site.register(contact_info_tabel),
admin.site.register(wish_list_table),
