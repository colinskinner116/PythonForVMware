file1 = open("vms.txt", "r")
text1 = file1.read()
listedvms = text1.split()

file2 = open("checker.txt", "r")
text2 = file2.read()
baddies = text2.split()

comparer = list(set(listedvms) & set(baddies))

for word in list(listedvms):
    if word in comparer:
        listedvms.remove(word)

outputter = open('output.txt', 'w')
        
for word in list(listedvms):
    outputter.write(word)
    outputter.write("\n")

outputter.close()


