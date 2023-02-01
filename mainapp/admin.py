from django.contrib import admin
from .models import roomIDModel

# Register your models here.
@admin.register(roomIDModel)
class staffs(admin.ModelAdmin):
	list_display = ('roomid', 'createdBy')
	ordering = ('roomid',)
	search_fields = ('roomid', 'createdBy')
