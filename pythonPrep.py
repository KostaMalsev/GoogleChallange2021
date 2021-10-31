
#loops example
def loops(start,finish)
  
  i = 1
  while i < 6:
    print(i)
    i += 1
  
  fruits = ["apple", "banana", "cherry"]
  
  for x in fruits:
    print(x)


#Conditions examples:
def conditions()

  a = 33
  b = 200
  if b > a:
    print("b is greater than a")


def dataStructures()

  #Arrays:
  cars = ["Ford", "Volvo", "BMW"]
  print cars[0]
  x = len(cars)
  
  #Classes:
  class MyClass:
  
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def myfunc(self):
      print("Hello my name is " + self.name)
    
    x = 5 #class memeber
  
  p1 = MyClass('bar',4)
  print(p1.x)
  print(p1.myfunc)
  
  #json:
  import json
  x =  '{ "name":"John", "age":30, "city":"New York"}'
  # parse x:
  y = json.loads(x)
  # the result is a Python dictionary:
  print(y["age"])
  
  
  #Sets:
  myset = {"apple", "banana", "cherry"}
  for x in myset:
    print(x)
  
  #Dictionaries: (no multiples allowed)
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  
  itemFromDictionary = thisdict.get("model")
    
  #get list of keys
  x = thisdict.keys()
  
  #Set value to dictionary
  car["color"] = "white"
  
  #Touples:
  mytuple = ("apple", "banana", "cherry")
  secondElement = mytuple[1]
  
  #Return the third, fourth, and fifth item:
  thistuple[2:5]
  

  
  


  
  
  
  
  
  
  
  
  

    
    

  
    
  
  


      
