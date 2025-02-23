#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name 
        self.breed = breed    
    def introduction(self):
      print(f"My name is {self.name}. I am a {self.breed}")  

dog1 = Dog("Scooby")   
dog2 = Dog("Jewel", "Dalmatian")
dog3 = Dog("Bolt", "German Shepherd")
dog4 = Dog("Odie", "Long-eared beagle")

print(dog1.breed)
print(dog2.breed)
print(dog3.name)
dog1.introduction()
dog2.introduction()
dog3.introduction()
dog4.introduction()
