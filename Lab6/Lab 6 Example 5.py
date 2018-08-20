word_list = ['First', 'Second', 'Third', "Fourth"]
out_file=open('outFile.txt', 'w')
for word in word_list:
    out_file.write(word + ' line\n')
out_file.close()