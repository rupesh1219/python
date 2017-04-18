###############################################################################
# longest substring without repetition
# for example,
# 'abcabbda' longest substring without repitition is abc
# 'bbbbb' longest substring without repitition is b
###############################################################################


def longest_substring(string_item):
    '''
    return longest substring without
    repitition
    '''
    string_new = string_item[0]
    list_len = []
    for j in range(1, len(string_item)):
        if string_item[j] not in string_new:
            print(string_item[j])
            string_new += string_item[j]
            print(string_new)
        else:
            list_len.append(len(string_new))
            string_new = string_item[j]
            print(string_new)
    return list_len

print(longest_substring('abcddetewryu'))
