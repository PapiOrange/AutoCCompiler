import os
print("Welcome to the automatic C compiler for Linux! Made by PapiOrange")
ninput = input("Create(0), or Compile(1)?")
if (str(ninput) == "Create" or str(ninput) == "0"):
	sinput = input("What is the name of the program?")
	os.system("touch " + str(sinput) + ".c")
	os.system("nano " + str(sinput))
elif (str(ninput) == "Compile" or str(ninput) == "1"):
	ainput = input("What program would you like to compile? (Please don't include the file type)")
	os.system("gcc -o " + str(ainput) + " " + str(ainput) + ".c")
	print("Now type ./" + str(ainput))
else:
	print("Error")
