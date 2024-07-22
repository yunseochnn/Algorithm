month = ["January" , "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon,d,y,t = input().split()
d = int(d[:-1])
y = int(y)
h,m = map(int,t.split(":"))
if y%400 == 0 or (y%4==0 and y%100!=0):
    days[1]=29
total_minute = sum(days)*24*60
mon_idx = month.index(mon)
cur = (sum(days[:mon_idx])+d-1)*24*60 + h*60 + m
print(cur/total_minute*100)