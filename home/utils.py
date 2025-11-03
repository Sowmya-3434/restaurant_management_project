import datetime
from .models import DailyOperatingHours

def get_today_operating_hours();
today = datetime.datetime.now().strftime('%A')

try:
    today_hours = DailyOperatingHours.objects.get(day=today)
    return (today_hours.open_time, today_hours.close_time)
except DailyOperatingHours.DoesNotExist:
    return (None, None)