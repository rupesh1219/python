'''
math quiz problem:
    The following program runs a math quiz consisting of 10
multiplication problems involving operands between 1 and 10
'''

from random import randint
correct = 0

for i in range(10):
    n1 = randint(1,10)
    n2 = randint(1,10)
    prod = n1*n2

    ans = int(input('what is %d times %d' % (n1,n2)))
    if ans == prod:
        print("that's right -- well done \n")
        correct = correct + 1
    else:
        print("No,Im afraid the answer is %d" % prod)

print("asked you 10 questions and you got %d correct answers" % correct)

a = correct

if a>=a/2:
    print("well done")
else:
    print("improve your performace")

'''
modify the above program so that users can choose how many questions they want
to be asked
'''

from random import randint

correct = 0
q1 = int(input('how many questions should I ask you?'))

for i in range(q1):
    n1 = randint(1,q1)
    n2 = randint(1,q1)
    prod = n1*n2

    ans = int(input('what is %d times %d' % (n1, n2)))
    if ans == prod:
        print("that's right -- well done \n")
        correct = correct + 1
    else:
        print("No,Im afraid the answer is %d" % prod)

print("asked you %d  questions and you got %d correct answers" % (ans,correct))

a = correct

if a>=a/2:
    print("well done")
else:
    print("improve your performace")


'''
let the user choose addition, substraction and multiplication or mixed
and find out the performance
'''

from random import randint

correct = 0
q2 = int(input("which type of operation do you need?"))

for i in range(10):
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    if q2 == 1:
        use = n1+n2
    if q2 == 2:
        use = n1-n2
    if q2 == 3:
        use = n1*n2

    ans = int(input("what's the value of %d %d %d" % (n1, q2, n2)))
    if ans == use:
        print("that's correct answer")
        correct = correct + 1
    else:
        print("No i am afraid %d is the answer" % use)

a = correct

if a>a/2:
    print("great job! answered %d correct")
else:
    print('you screwed up - cant you even solve elementory math')

