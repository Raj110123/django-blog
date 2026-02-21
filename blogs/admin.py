from django.contrib import admin
from .models import Category
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','author','is_featured','status','created_at')
    search_fields=('id','title','category__category_name','status')
    list_editable=('is_featured','status')
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)

