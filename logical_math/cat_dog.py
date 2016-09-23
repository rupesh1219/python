'''
how many min groups can be formed with the following rules :

There are N cats and M dogs
1.they sit in a straight line
2.cat cannot sit beside a cat and dog cannot sit beside a dog or they both cannot sit alone

Print -1 if they cannot form the groups
'''

def fun_catdog(N,M):
    if(N<=0 and M<=0):
        print('enter valid numbers')
    elif(N==M):
        print('one minimum group can be formed')
    elif(abs(N-M)<=N and abs(N-M)<=M):
        print('number of min groups formed are {}'.format(abs(N-M)))
    else:
        print('-1')

a = fun_catdog(7,4)
print(a)
