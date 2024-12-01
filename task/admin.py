from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'due_date', 'assignto')