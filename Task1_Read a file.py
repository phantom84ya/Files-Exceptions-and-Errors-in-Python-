try:
  file1 = open("sample.txt", "r")
  reading_file = file1.read()
  print("Reading the file content:")
  print(reading_file)
  file1.close()


except:
    print("The file 'sample.txt' is not found.")
  