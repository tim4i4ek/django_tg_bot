from django.contrib import admin
from .models import WorkingDay, WorkingHour, Work, Appointment

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):

    list_display = ('proposition', 'price', 'available')
    list_editable = ('price', 'available')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('client_name', 'date', 'time_slot', 'proposition', 'price')
    list_filter = ('date', 'proposition')

admin.site.register(WorkingDay)
admin.site.register(WorkingHour)