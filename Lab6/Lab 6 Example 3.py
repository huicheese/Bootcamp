temp_file=open("temp.txt","w")
print("first_line", file=temp_file)
print("second_line", file=temp_file)
temp_file.close()