###############################################################################
# given two numbers in the linked list format which are stored in reverse order
# add them and return it as a linked list
###############################################################################

####################################################
# learning linked list in python
# steps to learn:
# how to implement linked list in python
# how to print them
# how to iterate thorugh them
#
####################################################


class Linkedlist():

    def __init__(self, node=None, next=None):
        self.node = node
        self.next = next

    def __str__(self):
        return str(self.node)

    def print_backward(self, lst):
        return self.lst

learn = Linkedlist([1,2,3])
print(learn)
backward_list = Linkedlist.print_backward([1,2,3])
print(backward_list)

learn2 = Linkedlist(1,2)
print(learn2)
