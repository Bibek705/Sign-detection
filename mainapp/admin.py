from django.contrib import admin
from .models import usersModel

# Register your models here.
@admin.register(usersModel)
class users(admin.ModelAdmin):
	list_display = ('uid', 'name', 'role', 'channel')
	ordering = ('channel','role','uid','name',)
	search_fields = ('uid', 'name', 'role', 'channel')
