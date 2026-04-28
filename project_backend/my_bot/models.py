from django.db import models


class WorkingDay(models.Model):

    DAY_CHOICES = [
        (0, 'Понеділок'), (1, 'Вівторок'), (2, 'Середа'),
        (3, 'Четвер'), (4, 'Пятниця'), (5, 'Субота'), (6, 'Неділя'),
        ]

    day_of_week = models.IntegerField(choices=DAY_CHOICES, unique=True)
    start_time = models.TimeField(verbose_name="Початок роботи")
    end_time = models.TimeField(verbose_name="Кінець роботи")
    is_working = models.BooleanField(default=True, verbose_name="Робочий день?")

    def __str__(self):
        return f"{self.get_day_of_week_display()}: {self.start_time}-{self.end_time}"

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"

class Appointment(models.Model):
    # Запис клієнта на конкретну дату і час
    client_name = models.CharField(max_length=100, verbose_name="Ім'я клієнта")
    client_tg_id = models.BigIntegerField(verbose_name="Telegram ID")
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name="Послуга")
    date = models.DateField(verbose_name="Дата запису")
    time_slot = models.IntegerField(verbose_name="Година запису")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення запису")

    def __str__(self):
        return f"{self.date} о {self.time_slot}:00 — {self.client_name}"

    class Meta:
        verbose_name = "Запис"
        verbose_name_plural = "Записи"