
from datetime import datetime, timedelta
GIGASECOND = timedelta(seconds=10**9)
def add(moment: datetime) -> datetime:
    return moment + GIGASECOND