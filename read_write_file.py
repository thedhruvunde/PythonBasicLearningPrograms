#Writing File
f = open("/home/dhruv/Documents/Python/SelfMadePrograms/read_write_files/File.txt", "w")
f.write("I Love Python")
f = open("/home/dhruv/Documents/Python/SelfMadePrograms/read_write_files/File.txt", "a")
f.write("\nI Love JavaScript")
print("File Written!")
f.close()
#Reading File
f = open("/home/dhruv/Documents/Python/SelfMadePrograms/read_write_files/File.txt", "r")
print(f.read())
f.close()
