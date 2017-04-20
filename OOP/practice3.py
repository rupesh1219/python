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
