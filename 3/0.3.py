a = int(input('nhập số a '))
b = int(input('nhập số b '))
c = range(a-1,b)
for i in c:
    i = i +1
    if (i%5 == 0) and (i%3 == 0):
        print(' FizzBuzz ',i )
    elif (i%3 == 0):
        print("Fizzz",i )
    elif (i%5 == 0):
        print(" Buzz",i)
    else :
        print('unknow',i)