#from django.contrib import admin

# Register your models here.

#from django.contrib import admin

# Register your models here.

'''from django.contrib import admin
from .models import Customer, Category, File

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(File)


from django.contrib import admin
from .models import Customer, Category, File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    filter_horizontal = ('customers',)  # Allows for multi-select of customers

admin.site.register(Customer)
admin.site.register(Category)
'''

from django.contrib import admin  # type: ignore
from .models import Customer, Category, File
from inventory.models import Computer

class FileInline(admin.TabularInline):
    model = File.customers.through  # Intermediate model for ManyToMany
    extra = 0  # Do not show any extra empty forms

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    inlines = [FileInline]  # Display associated files inline

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

'''@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file_download_link')  # Add a custom column for download link
    filter_horizontal = ('customers',)

    def file_download_link(self, obj):
        return f'<a href="{obj.upload.url}" download>Download</a>'
    
    file_download_link.allow_tags = True  # Allow HTML to be rendered in this column
    file_download_link.short_description = 'Download Link'  # Column title in the admin

'''
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file_download_link')  # Ensure this is in the list_display

    def file_download_link(self, obj):
        # Ensure the file path is correct
        return f'<a href="{obj.upload.url}" download>Download</a>'
    
    file_download_link.allow_tags = True  # Allow HTML rendering
    file_download_link.short_description = 'Download Link'


