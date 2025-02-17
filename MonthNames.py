# Exercise 1. Name your file: MonthNames.py Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year. An example run of the program (numbers in bold are typed in by the user) Enter the month: 3 Month 3 is March

num=int(input('Enter the month:'))
if num==1:
    print(f'Month 1 is January')
elif num==2:
    print(f'Month 2 is February')
elif num==3:
    print(f'Month 3 is March')
elif num==4:
    print(f'Month 4 is April')
elif num==5:
    print(f'Month 5 is May')
elif num==6:
    print(f'Month 6 is June')
elif num==7:
    print(f'Month 7 is July')
elif num==8:
    print(f'Month 8 is August')
elif num==9:
    print(f'Month 9 is September')
elif num==10:
    print(f'Month 10 is October')
elif num==11:
    print(f'Month 11 is November')
elif num==12:
    print(f'Month 12 is December')
else:
    print('Invalid entry.Enter a number between 1 & 12.')