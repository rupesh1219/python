###############################################################################

# write a python class with two methods get_string and print_string. get_string
# accepts a string from the user and print_string prints the string in upper
# case

class Two_methods():

    def __init__(self, input_from):
        self.input_from = input_from

    def put_string(self):
        return self.input_from.upper()

upper_string = Two_methods(input('enter a string:'))
print(upper_string.put_string())


########
# OR
########

class Two_methods1():

    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input('enter a string:')

    def put_string(self):
        return self.str1.upper()


string_input = Two_methods1()
string_input.get_string()
put_string_out = string_input.put_string()
print(put_string_out)
