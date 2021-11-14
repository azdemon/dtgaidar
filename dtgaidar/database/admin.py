from django.contrib import admin
from .models import Base
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BookResource(resources.ModelResource):
    class Meta:
        model = Base

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Base, BookAdmin)
