###############################################################################
# read an integer N
# without using any string methods print 123...N
###############################################################################


class Printfunction():

    def __init__(self, x):
        self.x = x

    def printnum(self):
        '''
        print the sequence
        '''
        for i in range(self.x + 1):
            print(i, end='')


print_num = Printfunction(int(input('enter a number:')))
print_num.printnum()
