import math
r = 5
volume = 4 / 3 * math.pi * (r**3)
print(volume)

books = 60
price = 24.95
sale = 0.4
ship = 3
ship1 = 0.75
total = books * price * (1 - sale) + ship + ship1 * (books - 1)
print (f'total: {total:.2f} USD')

hour = 6
minutes = 52
minutes1 = 8
second1 = 15
minutes2 = 7
second2 = 12
minutes3 = 8
second3 = 15

totalwalkingtime = minutes1 + minutes2 * 3 + minutes3 + minutes
totalwalkingtime1 = second1 + second2 * 3 + second3
if (totalwalkingtime1 > 60):
    totalwalkingtime1 = totalwalkingtime1 % 60
    totalwalkingtime = totalwalkingtime + 1

if (totalwalkingtime > 60):
    totalwalkingtime = totalwalkingtime % 60
    hour = hour + 1

print(f'time you go back to eat breakfast: {hour}:{totalwalkingtime}:{totalwalkingtime1}')