from django.db import models
import datetime
class WorkingDay(models.Model):

    day_index = models.IntegerField(verbose_name="Номер дня тижня (0-6)")
    is_working = models.BooleanField(default=True, verbose_name="Робочий день")
    is_holiday = models.BooleanField(default=False, verbose_name="Вихідний/Свято")

    def get_available_slots(self, target_date):

        all_slots = self.hours.all().values_list('hour', flat=True)

        booked_slots = Appointment.objects.filter(
            date=target_date
        ).values_list('time_slot', flat=True)


        available = [slot for slot in all_slots if slot not in booked_slots]
        return sorted(available)

    def __str__(self):
        days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П’ятниця', 'Субота', 'Неділя']

        status = " (Робочий)" if self.is_working else " (Вихідний)"
        return f"{days[self.day_index]}{status}"

    class Meta:
        verbose_name = "Графік: День"
        verbose_name_plural = "Графік: Дні"
        ordering = ['day_index']

class WorkingHour(models.Model):

    working_day = models.ForeignKey(WorkingDay, on_delete=models.CASCADE, related_name='hours')
    hour = models.IntegerField(verbose_name="Година (0-23)")

    def __str__(self):
        return f"{self.hour}:00"

    class Meta:
        verbose_name = "Робоча година"
        verbose_name_plural = "Робочі години"
        ordering = ['hour']

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва послуги")
    price = models.IntegerField(verbose_name="Ціна (грн)")
    description = models.TextField(blank=True, verbose_name="Опис послуги")

    def __str__(self):
        return f"{self.name} — {self.price} грн"

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"

class Appointment(models.Model):

    client_name = models.CharField(max_length=100, verbose_name="Ім'я клієнта")
    client_tg_id = models.BigIntegerField(verbose_name="Telegram ID")
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name="Послуга")
    date = models.DateField(verbose_name="Дата запису")
    time_slot = models.IntegerField(verbose_name="Година запису")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення запису")
    is_approved = models.BooleanField()



    def __str__(self):
        return f"{self.date} о {self.time_slot}:00 — {self.client_name}"

    class Meta:
        verbose_name = "Запис"
        verbose_name_plural = "Записи"


