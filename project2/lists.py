mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)

print ("Print Explicit Values")
print("Mylist[0] = %d" % mylist[0])
print("Mylist[1] = %d" % mylist[1])
print("Mylist[2] = %d" % mylist[2])

print("\nPrint Using 'for' loop")
for x in mylist:
	print ("Mylist[x] = %s" % (mylist[x - 1]))

print("\nPrint using 'for' loop & 'range'")
for i in range(len(mylist)):
	print ("Mylist[%s] = %s" % (i, mylist[i]))

i = 0

print("\nPrint using 'while' loop")
while (i < len(mylist)):
	print ("Mylist[%d] = %d" % (i, mylist[i]))
	i = i + 1

print("\n------------------------------------------------")

print("Print length of list")
nlist = []
nlist.append(5)

print("Mylist contains %d objects" % (len(mylist)))
print("nlist contains %d objects" % (len(nlist)))

#TESTING

if (nlist.count(5) == 10 and mylist.count(3) == 10):
	print ("Almost There...") 

print("\n------------------------------------------------")

print("Print a tuple")
tub = (3, 5, 6, "hello")
print tub[0:]

print("\n------------------------------------------------")

print("Dictionary")
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

for name, number in phonebook.iteritems():
	print("%s's Number is %d" % (name, number))

del phonebook["John"]