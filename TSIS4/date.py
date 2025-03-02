from datetime import datetime, timedelta

print("Subtract five days:", datetime.now() - timedelta(days=5))

today = datetime.now().date()
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

print("Datetime without microseconds:", datetime.now().replace(microsecond=0))

d1 = datetime(2024, 2, 10, 12, 0, 0)
d2 = datetime(2024, 2, 5, 10, 30, 0)
print("Difference in seconds:", int((d1 - d2).total_seconds()))
