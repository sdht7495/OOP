class Sieunhan:
     name = str
     weapon = str
     color = str

     def __init__(self, name="hao", weapon="sword", color="red"):
          self.name = name
          self.weapon = weapon
          self.color = color

     def __str__(self):
        return"(%s,%s,%s)" % (self.name, self.weapon, self.color)

     def Read(self):
        self.name = input("enter superhero name: ")
        self.weapon = input("enter superhero weapon: ")
        self.color = input("enter superhero color: ")

sieunhanA = Sieunhan()
sieunhanA.Read()
print(sieunhanA)

sieunhanB = Sieunhan()
sieunhanB.Read()
print(sieunhanB)
