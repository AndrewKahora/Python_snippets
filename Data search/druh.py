name = open("work.txt" , "a+")
newname = raw_input("What is your name?")
read = name.read()
if type(newname) == str:
    name.write(newname + "\n")
    name.close()
elif newname in read:
    print "newname"
