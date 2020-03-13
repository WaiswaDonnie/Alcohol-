class Person:
    def __init__(self):
        self.name=input("Enter Your Name\n\t")
        self.age = int(input("Enter User AGE\n\t"))
    
    def drink_age_calculator(self):
        self.years_left= 18 - self.age  
        print(self.name,",you are left with ",self.years_left,"year/s"," to drink\n\t")
try:
    r1=Person()
    if r1.age>=18 and r1.age<100:
        print(r1.name,",you are allowed to drink")
    elif r1.age<18:
        user_choice = input(r1.name + ",do you have consent from any of your parent Y/N \n\t")
        if user_choice=='Y' or user_choice=='y':
            print(r1.name,",you are allowed to drink only one bottle")
        else:
            r1.drink_age_calculator()
    else:
        print("Invalid age group")
#Handling errors
except(ValueError):

    print("Age Error:\n\t\t Age cannot contain a string or float data type")
