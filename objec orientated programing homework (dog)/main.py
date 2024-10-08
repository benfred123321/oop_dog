class Dog:

    def __init__(self):
        self.name = "woofers"
        self.age = 8
        self.oners_name = "bob"
        self.coulor_of_fur = "pink"

    def show_details(self):
        print("the dogs details are: ")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("oners name is: ",self.oners_name)
        print("the couler of the dogs fur is: ",self.coulor_of_fur)

    def update_details(self):
        self.name = input("what is the name of the dog? ")
        self.age  = int(input("what is the age of the dog? "))
        self.oners_name = input("what is the oners name? ")
        self.coulor_of_fur = input("what is the coulor of the dogs fur? ")

dog1 = Dog()

dog1.show_details()
dog1.update_details()
dog1.show_details()
