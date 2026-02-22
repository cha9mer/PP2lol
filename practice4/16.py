from datetime import datetime, timedelta, timezone
import re

def parse_datetime(line):
    date_part, tz_part = line.rsplit(" ", 1)
    dt = datetime.strptime(date_part, "%Y-%m-%d %H:%M:%S")
    
    m = re.match(r"UTC([+-])(\d{2}):(\d{2})", tz_part)
    sign, hours, minutes = m.groups()
    offset_minutes = int(hours)*60 + int(minutes)
    if sign == "-":
        offset_minutes = -offset_minutes
    
    tz = timezone(timedelta(minutes=offset_minutes))
    return dt.replace(tzinfo=tz)

start = parse_datetime(input())
end = parse_datetime(input())

start_utc = start.astimezone(timezone.utc)
end_utc = end.astimezone(timezone.utc)

duration = int((end_utc - start_utc).total_seconds())
print(duration)