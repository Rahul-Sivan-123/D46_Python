# Exercise 3. Name your file: BodyMassIndex.py Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters: BMI= weight(kg)/height2(m2) BMI Weight Status Categories table BMI range - kg/m2 Category Below 18.5 Underweight 18.5 -24.9 Normal 25 - 29.9 Overweight 30 & Above Obese An example run of the program (numbers in bold are typed in by the user) Enter your weight in (kg): 75 Enter your height in (m): 1.70 Your BMI is: 25.95 You are in the “overweight” range.

weight=float(input('Enter you weight in (kg):'))
height=float(input('Enter your height in (m):'))
bmi=weight/(height**2)
if bmi < 18.5:
    print('You are in "Underweight" range.')
elif 18.5<= bmi <= 24.9:
    print('You are in "Normal" range.')
elif 25<= bmi <= 29.9:
    print('You are in "Overweight" range.')
else:
    print('You are in "Obese" range.')