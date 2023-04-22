# OBEJECT ORIENTED PROGRAMMING IN PYTHON.

# CREATING A CLASS,OBJECT....
'''class Person:
    name="Benson"
    occupation="Software Developer"
    networth=50
    print("Person's name is",name,",his occupation is",occupation,"and his networth is",networth)

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        print("Name is",self.name,"Roll number is ",self.roll)
    def info(self):
        print(self.name,"is a",self.occupation)


    def bio(self):
        print(self.name,"I belong to 'bio' function")
print(Person.name)
Person.name = "Rohan"  #This is used to change name by accessing class
print(Person.name)
b=Person("Divya",2)  #Object instantiation(Here these arguments are passed in __init__ constructor.)
a=Person("Ayaan",23)  #Object Instantiation (Here these arguments are passed in __init__ constructor.)
a.name="Rahul"  #This is used to change the name
a.occupation="Designer"  #This is used to change the occupation
a.networth=25  #This is used to change the networth
print(a.name,"-->",a.occupation,"-->",a.networth)
print(b.name)
a.info()
a.bio()'''


# CREATING A CLASS,OBJECT....
'''class Employee():
    emp_name="Alex"
    emp_blood_grp="O"
    emp_loc="France"
    emp_salary=300

    def __init__(self,name,age,fav_dish):
        self.name=name
        self.age=age
        self.fav_dish=fav_dish
        print("Name is ",self.name,",Age is",self.age,",Favourite dish is",self.fav_dish)

    def get_info(self):
        print("Employee's name is",self.emp_name,",Employee's blood group is",self.emp_blood_grp,",Location is",self.emp_loc,",Salary is",self.emp_salary)



a=Employee("SpiderMan",33,"Hakka Noodles")
print(a.emp_name)
a.get_info()'''


#INHERITANCE and Polymorphism Example.
'''class GrandFather():  #This is the base/Parent class.
    g_height=6
    g_bike="Harley Davidson"
    

    def __init__(self):
        print("This's GrandFather's init constructor.")
        print("I am GrandFather.I am the Base class!")


class Father(GrandFather):   #Class Father inherits from Class GrandFather.(Single Inheritance)
    g_bike="BMW" #Each new class can've it's own attributes,it can also inherit attributes of its base class.
    f_height=7
    

    def __init__(self):
        print("This is Father's init constructor!")   #Most recent init constructor will be given as output.
        print("Hi there!!!,This's Father Class.I inherit from my father i.e Grandfather.I inherit by single inheritance.")
        super().__init__() # super().__init__ function returns objects represented in the parent's class

class Child(Father):#Multilevel Inheritance
    g_bike="Roadster"  #Polymorphism Base class and derived class all 've g_bike,so the most recent one 'll be printed
    c_height=6.8
    
    def __init__(self):
        print("This is Child Class's init constructor.")
        print("Hi,I am Child Class,I Inherit from my Father and Grandfather;I inherit by Multilevel Inheritance.")
        super().__init__()  # super().__init__ function returns objects represented in the parent's class

a=Child()
print(a.g_bike)
print(a.g_height)
print(a.c_height)
b=Father()
print(b.g_bike)'''

# --------------------------------------------------------------------------------------------------------------------


# POLYMORPHISM Example.

'''class India():
    neighbour="Pakistan"

    def __init__(self,animal,bird):
        self.animal1=animal#We can use any name instead of animal like in this case we've given self.animal1
        self.bird1=bird
        print("India is in Asia.India's nieghbour is",self.neighbour,".India's National animal is",self.animal1,"and National bird is",self.bird1)


    def capital(self):
        print("Delhi is the capital of India.")
    def stage(self):
        print("India is a developing country.")

class USA():
    neighbour="Canada"
    def __init__(self,animal,bird):
        self.animal2=animal
        self.bird2=bird
        print("USA is in North America.",self.neighbour,"is USA's neighbour.",self.animal2,"is the National animal",self.bird2,"is the National bird.")

    def capital(self):
        print("Washington D.C is the capital of USA.")
    def stage(self):
        print("USA is a developed country.")


# a=India("Tiger","Peacock")
# a.capital()
# a.stage()
# b=USA("American Bison","Bald Eagle")
# b.capital()
# b.stage()


a = India("Tiger","Peacock")
b = USA("American Bison","Bald Eagle")
for country in (a,b):   #using this loop we call the required functions of both the classes.
    country.capital()
    country.stage()'''

# ------------------------------------------------------------------------------------------------------------------------



# HASATTR FUNCTION (USED TO CHECK WHETHER AN ATTRIBUTE IS PRESENT IN THE CLASS MENTIONED OR NOT.)
'''class Person:
    name = "Benson Jose"
    age = 20
 
# initializing object
a = Person()

# using hasattr() to check name
print("Does name exist ? ",hasattr(a, 'name'))
 
# using hasattr() to check age
print("Does motto exist ? ",hasattr(a, 'age'))

print("Present??-->",hasattr(a,"gender"))
'''
# --------------------------------------------------------------------------------------------------------------------



# ABSTRACT METHOD IN PYTHON.(main goal of the abstract base class is to provide a standardized way to test whether an object adheres to a given specification.)
'''
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.length=8
        self.breadth=9
    def area(self):
        return f"The area is {self.length*self.breadth} sq.units"

class Square(Shape):
    def __init__(self):
        self.side=4
        # return f"The area of Square is{self.side*self.side}sq.units"   #DOUBT*****************************************

    def area(self):
        return f"The area of Square is {self.side*self.side} sq.units"
        

a=Rectangle()
print(a.area())
b=Square()
print(b.area())
'''

# 


# ABSTRACT METHOD IN PYTHON.
'''from abc import ABC, abstractmethod
class Football(ABC):  #Abstract class
    @abstractmethod  #abstract method
    def name(self):
        pass
    @abstractmethod
    def weight(self):
        pass

class Playerone(Football):
    def name(self):
        print("Neymar")
    def weight(self):
        print(70)

class Playertwo(Football):
    def name(self):
        print("Benson")
    def weight(self):
        print(65)

a=Playerone()
a.name()  #Here you don't need to print,--->a.name() is sufficient;If you add print() None 'll be added in the output.
a.weight()

b=Playertwo()  
b.name()  #Here you don't need to print,--->a.name() is sufficient;If you add print() None 'll be added in the output.
b.weight()'''



# PYTHON PROGRAM TO DEMONSTRATE PROTECTED MEMBERS...01
'''
# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
'''




#PYTHON PROGRAM TO DEMONSTRATE PROTECTED MEMBERS...02
# _a(protected)
# __a(private)'''
'''
class Base:
    def __init__(self):
        print("Parent class constructor is called.")
        self._a=2  #Protected member
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)

x=Derived()
print(x._a)
'''


# doubt***************************************PRIVATE---MEMBERS************************************************************************
 










