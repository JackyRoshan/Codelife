class Person():
    Name = 'Jacky'
    Age = 22
    Weight = 80
    Height = 183

    def _init_(self,age,weight,height):
        self.Age = age
        self.Weight = weight
        self.Height = height

    def get_person_data(self):
        print('My name is Jacky')
        print('My age is',self.Age)
        print('My height is',self.Height)
        print('My weight is',self.Weight)

print('Oringinal data')

print(Person.Age)
print(Person.Weight)
print(Person.Height)

print('Initial the data?')
Person._init_(Person,24,75,190)

print(Person.get_person_data(Person))