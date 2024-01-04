from django.contrib import admin

from web.models import Tasks,Students


class TaskAdmin(admin.ModelAdmin):
    list_display=["title","date_time","is_completed","is_deleted","student"]

admin.site.register(Tasks,TaskAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display=["id","first_name","last_name","st_class","division","phone","email"]

admin.site.register(Students,StudentAdmin)
