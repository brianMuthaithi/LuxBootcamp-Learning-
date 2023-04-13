# Write a file
f = open("session.txt", "w")
f.write("Hello class \n")
f.writelines("This is a python class \n")
f.writelines("Beware of women in Corporate! \n")

# Read data in a file
f = open("session.txt", "r")
print(f.readlines())
f.seek(0)           #print from line 2
print(f.read(1))    #Print to line 0

#Append text in files
header = "Write Data"
f = open("session.txt", "a")
f.write("Tomorrow \n")
f.close()