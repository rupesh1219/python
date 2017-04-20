###############################################################################

# write a python class to find pair of elements whose sum is equal to target


class Sum_target():

    def __init__(self, lst, target):
        '''
        initializing a class
        '''
        self.lst = lst
        self.target = target

    def result(self):
        for i in range(len(self.lst)):
            for j in range(i+1, len(self.lst)):
                if self.lst[i] + self.lst[j] == self.target:
                    return (self.lst[i], self.lst[j])


target1 = Sum_target([1,2,3,4], 7)
print(target1.result())
