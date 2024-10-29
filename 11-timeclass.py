class Time:
	"""defines the class"""

time = Time()
time.hour = 6
time.min = 30
time.sec = 30

def print_time(t):
	print('%.2d : %.2d : %.2d' %(t.hour, t.min, t.sec))

def is_after(t1, t2):
	d1 = t1.hour*3600 + t1.min*60 + t1.sec
	d2 = t2.hour*3600 + t2.min*60 + t2.sec
	print('second values are: %d and %d' %(d1, d2))
	print(d1 > d2)		# display True if t1 > t2 in absolute seconds values

h = input('Enter hours: ')
m = input('Enter minutes: ')
s = input('Enter seconds: ')

time1 = Time()
time1.hour = int(h)
time1.min = int(m)
time1.sec = int(s)

print_time(time)
print_time(time1)
is_after(time, time1)
