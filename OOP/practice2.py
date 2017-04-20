###############################################################################

# write a python class to find the list all the sum of three elements is zero

class Sum_three_zero():

    def __init__(self, lst, target):
        self.lst = lst
        self.target = target

    def sum_zero(self):
        for i in range(len(self.lst)-2):
            for j in range(i+1, len(self.lst)-1):
                for k in range(j+1, len(self.lst)):
                    if self.lst[i] + self.lst[j] + self.lst[k] == 0:
                        result = (self.lst[i], self.lst[j], self.lst[k])
                        yield result


target_zero = Sum_three_zero([-1,1,0,3,4,5,-9], 0)
print(target_zero.sum_zero())

for i in target_zero.sum_zero():
    print i
