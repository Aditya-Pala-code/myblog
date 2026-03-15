from django.contrib import admin

# Register your models here.

from .models import Post,Contact

admin.site.register(Post) 


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)

admin.site.register(Contact, ContactAdmin)