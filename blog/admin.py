from django.contrib import admin
from .models import Post, Author, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",) # in the admin pannel you filter by these
    list_display = ("title", "date", "author",) # in the admin pannel you can now see the title date and author instead of ojbect#1
    prepopulated_fields = {"slug": ("title",)}  #Making the Slug based on title

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)