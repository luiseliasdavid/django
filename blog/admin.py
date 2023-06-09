from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','modified')
    list_display=('title','created','modified')
    ordering = ('created',)  # Ordenar en orden descendente (-) por fecha de creación

admin.site.register(Post,PostAdmin)