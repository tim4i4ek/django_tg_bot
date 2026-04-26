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
        verbose_name = "Графік роботи"
        verbose_name_plural = "Графіки роботи"