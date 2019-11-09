from django.contrib import admin
from .models import Student , Eventlst , Pointstable
class StudentAdmin(admin.ModelAdmin):
	list_display = ('admno','sname','gender','category','house','sclass','ssec','event1','event2','event3')

class EventAdmin(admin.ModelAdmin):
	list_display = ('eventname','status')
	ordering     =('eventname',)

class PointsAdmin(admin.ModelAdmin):
	list_display = ('admno','event','points')


admin.site.register(Student, StudentAdmin)
admin.site.register(Eventlst, EventAdmin)
admin.site.register(Pointstable, PointsAdmin)