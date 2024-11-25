'''from django.contrib import admin

from .models import Article, Category, Tag

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # Display all relevant fields in the list view
    list_display = ('title', 'category', 'created_at', 'updated_at')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag')  # Display category name

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)  # Display category name

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag')  # Display category name'''

from django.contrib import admin # type: ignore
from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    # Display all relevant fields in the list view
    list_display = ('title', 'category', 'created_at', 'updated_at')
    
    # Allow searching by title and content
    search_fields = ('title', 'content')

    # Add filters for easy navigation
    list_filter = ('category', 'tags')

    # Enable display of tags in the list view
    filter_horizontal = ('tags',)

    # Organize fields in a fieldset for a cleaner layout in the detail view
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'content', 'category', 'tags')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Collapsible section for optional organization
        }),
    )

    # Make 'created_at' and 'updated_at' read-only to prevent manual changes
    readonly_fields = ('created_at', 'updated_at')

# Register ArticleAdmin with the Article model
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)