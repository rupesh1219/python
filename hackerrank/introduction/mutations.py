###############################################################################
# given:
# string, positon, character
# replace a string with given character
###############################################################################


class replace_character():

    def __init__(self, string, position, character):
        self.string = string
        self.position = position
        self.character = character

    def replacing(self):
        '''
        retruns the repalced
        string
        '''
        return self.string[:self.position] + self.character + \
            self.string[self.position+1:]


replaced_output = replace_character('rupesh', 3, 'k')
print(replaced_output.replacing())
