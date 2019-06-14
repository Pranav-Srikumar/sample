yr=int(input())
if((yr%4==0) and (yr%100!=0)) or (yr%400==0):
    print("Its a leap year")
else:
    print("not a leap year")
