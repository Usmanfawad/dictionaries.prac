phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook["John"])
print(phonebook)
print(phonebook.items())
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is: %d" % (name, number))


phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
for x,y in phonebook.items():
    print("Phone number of %s is: %d" %(name,number))

for x in range(3):
    name=['usman','fawad','ali']
    age=(19,20,21)
    print("%s's age is: %d"% (name[x],age[x]))

xxx={}
x= input("Enter field name: ")
y= input("Enter field value: ")
z=input("Do you want to continue? y/n ")
while z!='n':
    x= input("Enter field name: ")
    y= input("Enter field value: ")
    z=input("Do you want to continue? y/n ")
    xxx[x]=y
for g,h in xxx.items():
    print('{:<10} :{:<20}'.format(g,h))
    
