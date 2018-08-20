temp_file=open("temp1.txt","r")
#first_line_str=temp_file.readline()
#print(first_line_str)
for line_str in temp_file:
    print(line_str)
temp_file.readline()
temp_file.close()