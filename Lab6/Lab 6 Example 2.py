def uncompressed(compressed):
    uncompressed = ''
    for i in range(len(compressed)):
        if compressed[i].isdigit():
            uncompressed += int(compressed[i]) * compressed[i+1]
    return uncompressed

a=uncompressed('5a2b3c')
print(a)