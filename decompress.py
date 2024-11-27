def decompress(s):
    i = 0 
    result = ''

    for j in range(len(s)):
        if s[j].isalpha():
            num = s[i:j]
            char = s[j]
            result += str(char) * int(num)
            i = j + 1
    return (result)



s = '2a4b'
print(decompress(s))
