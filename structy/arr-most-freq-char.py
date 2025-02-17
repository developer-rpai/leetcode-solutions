def most_frequent_char(string):
    my_dict = {}
    for s in string:
        if s not in my_dict:
            my_dict[s] = 1
        else:
            my_dict[s] += 1

    max_count = float('-inf')
    letter = ''
    for  key, value in my_dict.items():
        if value > max_count:
            max_count = value
            letter = key

    return letter



s = 'riverbed'
print(most_frequent_char(s))