from datetime import datetime, timedelta, timezone
import re

def parse_datetime(line):
    date_part, tz_part = line.split()
    
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    m = re.match(r"UTC([+-])(\d{2}):(\d{2})", tz_part)
    sign, hours, minutes = m.groups()
    offset_minutes = int(hours) * 60 + int(minutes)
    if sign == "-":
        offset_minutes = -offset_minutes
    
    tz = timezone(timedelta(minutes=offset_minutes))
    
    dt = dt.replace(tzinfo=tz)
    return dt

dt1 = parse_datetime(input())
dt2 = parse_datetime(input())

diff_seconds = abs((dt1.astimezone(timezone.utc) - dt2.astimezone(timezone.utc)).total_seconds())

full_days = int(diff_seconds // 86400)

print(full_days)