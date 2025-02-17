def anagrams(s1, s2):
    return helper(s1) == helper(s2)


def helper(string):
    my_dict = {}

    for s in string:
        if s not in my_dict:
            my_dict[s] = 1
        else:
            my_dict[s] += 1
    return my_dict



s1 = 'cats'
s2 = 'sta3c'
print(helper(s2))

print(anagrams(s1,s2))

