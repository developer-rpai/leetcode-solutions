















def uncompress(s):
    i = 0
    result = ''

    for j, value in enumerate(s):
        if value.isalpha():
            result += int(s[i:j]) * value
            i = j + 1
    return result
 

s = '2a4b'
print(uncompress(s))
