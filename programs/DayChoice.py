'''

'''
D=input().strip()
N=int(input())

weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

start_index=weekdays.index(D)

day_index=(start_index+(N-1))%7

print(weekdays[day_index])
