###############################################################################
# split the string on ' ' delimiter and join using -
# for example 'this is a string'
# output: 'this-is-a-string'
###############################################################################


class Stringjoin():

    def __init__(self, x):
        self.x = x

    def input_string(self):
        '''
        return the string as
        needed
        '''
        list_words = self.x.split()
        string_output = ''
        for i in range(len(list_words)):
            if i != len(list_words)-1:
                string_output += list_words[i] + '-'
            else:
                string_output += list_words[i]
        return string_output

required_output = Stringjoin('this is a string')
print(required_output.input_string())
