#Used to store multiple data together
#[]initiated by double brackets
#List are indexed
#List are immutable meaning that they can always be changed
#List allows duplication
#List can store all data types mixed.
#One list can contain list within list
Fruits = ["Mangoes","Bananas","Cherries",["Green","Red"],"Apples","Melons"]
print (Fruits)

#Determining the lenght of the list
len(Fruits)
#The type
type(Fruits)
#accessing the index number of elements
#Index number starts from 0
#print(Fruits[2])
#Accesing the list from the end using a negative sign
#Accessing an element in a list within a list
#get green
print(Fruits[2][  1])

#Elements can be acces by stating the range
#Accessing the subset of list :index,position
print(Fruits[1:3])
Numbers = (1,2,3,4,5,6,78,9)
print(Numbers)
print(Numbers[1:7])
print(Numbers[-1:-4])
print(Numbers[3:])
print(Numbers[:4])

#Updating the list
#Adding the elements to a list
#Changing the element
Numbers[4]=int(10) 
#Extending the list
Numbers.insert(4,'100') 
#Adding the elements frm the end
#Using append
Numbers.append('100')
print(Numbers)


#Combination of more than one list
Gender =['Male','Female']
Class = ['First','second','Third','Subs']
Gender.extend(Class)
print(Gender)

Gender.remove('Male')
print(Gender)

Gender.clear()
print(Gender)


#Sorting list
#Sort the elements in an Ascending order.
#The elements wil be arranged from the smallest to the largest
# Sorting is important in a a state where te data is in bulk
# Te process is first just a click of a button    
Marks= (100,23,45,67,87,54,56,78)
Marks.sort()
#Using reverse sort does the opposite it arranges the elements
#in a descending order
#That is from the largest to the smallest
Marks.sort(reverse=True)
print(Marks)
 
#Sorting of strings follows the order of alphabets

names= ("Samantha","Nicole","Terry","Kibet")
names.sort()
print(names) 

#Copy list
#Copies the elements in one list to the other list
list1 = (1,2,3,4,5,6,7,8,9)
list2 = list1
print(list2)
#list1.pop()
print(list2)
list3 = list1.copy()
print(list3)





#Create list of five colours
#add new color at location 3
#Create a list of laptops by taking the input
#add new laptop at the starting
#Combine the list

Color =("Blue","Red","Orange","Magenta","Pale GReen")
print(Color)
Color[3] = "Maroon"
print(Color)


Laptop1 =input("First laptop")
Laptop2 =input("Second laptop")
Laptop3 =input("Third laptop")
Laptop4 =input("Forth laptop")

Laptop_list = (Laptop1,Laptop2,Laptop3,Laptop4)
Laptop_list[0]= "Toshiba"
print(Laptop_list)



