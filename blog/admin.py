from django.contrib import admin
from .models import Blog, Difficulty


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Difficulty)
