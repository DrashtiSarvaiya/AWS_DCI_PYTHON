#-------Creating a car inventory program-------#

#Defining the dictionary
#csv and copy are libraries of python
#CSV : A text file allows data to be saved in table structured format
#Copy() :It makes a deep copy of the data to store in memory by using a module called copy.
import csv 
import copy

#define a dictionary that will serve as your composite type for reading the tabular data
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#You will use a for loop to iterate over the initial keys and values of the dictionary.
#The items() function belongs to the dictionary data type. 
#The items() function tells the for loop to traverse the collection owned by the dictionary data type.
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
#Define an empty list to hold the car inventory that you will read
myInventoryList = []

#Copying the CSV file into memory
#"with open" which keeps a file open while you read data. 
#It will automatically close the CSV file when the code inside the with block is finished running.
#new way of formatting string i.e instead of using double quotation marks and .format to pass in the variables,you can use a single quotation mark and write in the variables between the "{}" symbols.
#csv.reader() is a function that you are using from the csv library
#append() function inserts a single element into an existing list.
#append() :The element will be added to the end of the old list rather than being returned to a new list.
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
currentVehicle = copy.deepcopy(myVehicle)

# A shallow copy refers, or points, to the storage location of the myVehicle dictionary variable.
#Without this line, you would have only one storage box, and only the last item in the list would be copied into memory. 
#This line makes sure that new storage boxes are created in memory to store the new tabular data that is being read.


#Printing the car inventory
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")