
#open two files, one with total vms to be deleted
#the other with vms found to either not exist or be powered on
#using a powercli script
file1 = open("vms.txt", "r")
text1 = file1.read()
listedvms = text1.split()

file2 = open("checker.txt", "r")
text2 = file2.read()
baddies = text2.split()
#baddies is so named because they don't belong on the 2bedeleted list

#make a list of only the values that are the same in both lists
comparer = list(set(listedvms) & set(baddies))

#remove the baddies from the master list
for word in list(listedvms):
    if word in comparer:
        listedvms.remove(word)

#output the results line by line to output.txt and you have your revised list!
outputter = open('output.txt', 'w')
        
for word in list(listedvms):
    outputter.write(word)
    outputter.write("\n")

outputter.close()


