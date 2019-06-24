from django.contrib import admin

from blog.models import Blog, Author, Comment, Tag

#admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Tag)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'categories')

  

