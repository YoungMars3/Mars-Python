 input text file
inputFile = "trial.txt"
# Opening the given file in read-only mode.
with open(inputFile, 'r') as filedata:
   # Read the file lines using readlines()
   inputFilelines = filedata.readlines()
   # storing the current line number in a variable
   lineindex = 1
   # Enter the line number to be deleted
   deleteLine = int(input("Enter the line number to be deleted = "))
   # Opening the given file in write mode.
   with open(inputFile, 'w') as filedata:
      # Traverse in each line of the file
      for textline in inputFilelines:
         # Checking whether the line index(line number) is
         # not equal to a given delete line number
         if lineindex != deleteLine:
            # If it is true, then write that corresponding line into file
            filedata.write(textline)
            # Increase the value of line index(line number) value by 1
            lineindex += 1
# Print some random text if the given particular line is deleted successfully
print("Line",deleteLine,'is deleted successfully\n')
# Printing the file content after deleting the specific line
print("File Content After Deletion :")
# Reading the file again in read mode
givenFile = open(inputFile,"r")
# Traversing the file line by line
for line in givenFile:
   # printing each line
   print(line)
# Closing the input file
filedata.close()