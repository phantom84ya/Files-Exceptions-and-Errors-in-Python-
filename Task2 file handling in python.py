text_to_write = input("Enter text to write to the file: ") #Hello Python 

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

text_to_append = input("Enter additional text to append: ") #Learning file handling in Python 

with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

print("Final content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
  