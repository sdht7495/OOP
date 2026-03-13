import time
time = int(time.time())
days = time // 86400
remaining = time % 84600

hours = remaining // 3600
remaining = remaining % 3600

minutes = remaining // 60
remaining = remaining % 60

second = remaining // 60
print(int(days), ':', int(hours), ':', int(minutes), ':', int(second))