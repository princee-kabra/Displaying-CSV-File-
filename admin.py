from django.contrib import admin
from.models import at
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(at)
class us(ImportExportModelAdmin):
	pass