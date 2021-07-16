class Person:
    
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = 0
        self.initialAge = initialAge
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
        else:
            initialAge =self.age

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        if self.age >= 13 and self.age<=18:
            print("You are a teenager.")
        if self.age >18:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge +=1
    

t = int(input())

Myclass = Person(t)
Myclass.amIOld()
Myclass.yearPasses()