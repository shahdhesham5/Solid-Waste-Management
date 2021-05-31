from django.contrib import admin

# Register your models here.
from .models import *



class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1

class TaskInline(admin.StackedInline):
    model=Project_task
    extra=5


class Project_CountryAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]
    search_fields = ['location']
    class Media:
        css = {
             'all': ('{{STATIC_URL}}admin/css/admin.css ',)
        }

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    search_fields = ['name']



admin.site.register(Project_Team)
admin.site.register(Project_Country,Project_CountryAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Project_task)
