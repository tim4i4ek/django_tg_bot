from django.contrib import admin
from .models import WorkingDay, WorkingHour, Service, Appointment

class WorkingHourInline(admin.TabularInline):
    model = WorkingHour
    extra = 5

@admin.register(WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
    list_display = ['day_index', '__str__', 'is_working']
    inlines = [WorkingHourInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['date', 'time_slot', 'client_name', 'is_approved']
    list_filter = ['is_approved', 'date']
    list_editable = ['is_approved']