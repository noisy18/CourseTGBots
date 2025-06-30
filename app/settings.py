from datetime import datetime
import pytz

# Settings parameters
timezone = pytz.timezone("Europe/Moscow")


# Functions
def get_current_time():
    return datetime.now(timezone)