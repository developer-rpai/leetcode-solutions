def compress(s):
    i = 0 
    count = 0
    result = ''
    for j, value in enumerate(s):
        
        if s[i] != s[j]:
            if count == 1:
                result +=   s[i]
            else:
                result += str(count) +  s[i]
            count = 0
            i = j

        if j == len(s)-1:
            if count == 0 :
                result += s[i]
            else:
                result += str(count+1) +  s[i]

        count += 1
    return result


s = 'ssssbbz'
print(compress(s))    