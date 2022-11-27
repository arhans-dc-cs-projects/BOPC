from datetime import date 

birthday = date(2009, 6, 12)
day = date(2022, 11, 22)

diff = day - birthday
print(diff.days)
