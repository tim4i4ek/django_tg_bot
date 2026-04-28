from datetime import datetime, timedelta
from my_bot.models import WorkingDay, Appointment


def get_available_dates(days_count=30):
    today = datetime.now().date()
    available_dates = []

    for i in range(days_count):
        check_date = today + timedelta(days=i)
        day_idx = check_date.weekday()

        working_day = WorkingDay.objects.filter(day_index=day_idx, is_working=True).first()

        if working_day:
            available_dates.append({
                'date': check_date,
                'weekday_name': working_day.__str__().split(" ")[0]
            })

    return available_dates


def get_free_hours_for_date(date_str):

    target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    day_idx = target_date.weekday()

    working_day = WorkingDay.objects.filter(day_index=day_idx, is_working=True).first()

    if not working_day:
        return []

    return working_day.get_available_slots(target_date)