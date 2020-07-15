import time

t = time.time()
year = int(t // 3600 // 24 // 365)
month = int((t - year*3600*24*365) // 3600 // 24 // 30)
day = int((t - year*3600*24*365 - month*30*24*3600) // 3600 // 24)
hour = int((t - year*3600*24*365 - month*30*24*3600 - day*24*3600) // 3600)
minute = int((t - year*3600*24*365 - month*30*24*3600 - day*24*3600 - hour*3600) // 60)
second = int((t - year*3600*24*365 - month*30*24*3600 - day*24*3600 - hour*3600 - minute*60))
print('approximate years = {}, approximate months = {}, approximate days = {}, hours = {}, minutes = {}, seconds = {}'.format(year, month, day, hour, minute,  second))


h = int((t - (t//3600//24)*3600*24)//3600)
m = int((t - (t//3600//24)*3600*24 - h*3600) // 60)
s = int(t - (t//3600//24)*3600*24 - h*3600 - m*60)

time_now = str(h) + ':' + str(m) + ':' + str(s)

print('number of days since the epoch = {}, and time now is : '.format(int(t//3600//24)) + time_now)


