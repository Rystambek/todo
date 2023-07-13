from django.contrib import admin

from .models import Task,Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',"description",'completed','user_id')
    list_filter = ('completed', 'created', 'updated')
    search_fields = ('title','description')
    ordering = ('title','completed','description')
    actions = ('mark_as_completed','mark_as_uncompleted')

    def user_id(self,obj):
        return f'{obj.user.id} - {obj.user.username}'
    
    @admin.action(description='mark as completed')
    def mark_as_completed(self,request,queryset):
        queryset.update(completed=True)
    
    @admin.action(description='mark as uncompleted')
    def mark_as_uncompleted(self,request,queryset):
        queryset.update(completed=False)

admin.site.register(Category)