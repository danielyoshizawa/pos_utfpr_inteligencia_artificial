def addPhotos(*imageList):
     for image in imageList:
          print("The file name to be sent is: {}".format(image))

addPhotos("foto1.jpg", "foto2.jpg", "foto3.jpg")
addPhotos("foto1.jpg", "foto3.jpg")
addPhotos("foto1.jpg")

def showName(name):
     print(name)

showName("John")
# showName()

def getCountryPopulation(country = "USA"):
     if(country == "USA"):
          return 331900000
     elif(country == "Brazil"):
          return 214300000
     elif(country == "China"):
          return 1412000000
     else:
          return "No data about this country" 

print(getCountryPopulation("Brazil"))
print(getCountryPopulation("China"))
print(getCountryPopulation())

def getBodyData(name):
     if(name == "Antônia"):
          return (1.76, 78.1)
     elif(name == "Luiza"):
          return (1.52, 89.6)
     elif(name == "Jennifer"):
          return (1.91, 77.3)
     else:
          return(0,0)

print(getBodyData("Antônia"))
print(getBodyData("Luiza"))
print(getBodyData("Jennifer"))
print(getBodyData("João"))

print(type(getBodyData("Antônia")))