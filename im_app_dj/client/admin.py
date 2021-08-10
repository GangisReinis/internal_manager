from django.contrib import admin
from client.models import *
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("company_name",)}

admin.site.register(attr_company, ClientAdmin)

admin.site.register(attr_employee)
admin.site.register(attr_asset)
admin.site.register(attr_related)
