from django.contrib import admin

# Register your models here.
from To_Do_list.models import ToDoList


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'due_date']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'due_date']
    readonly_fields = ['due_date']


admin.site.register(ToDoList, TodoAdmin)
