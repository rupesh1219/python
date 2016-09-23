str1 = str(input('enter a string:'))

def count_hi(str1):
    num_count = 0
    for i in range(len(str1)-1):
        if str1[i:i+2]=='hi':
            num_count += 1
    return num_count
print(count_hi(str1))
