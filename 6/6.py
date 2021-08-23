a = int(input('nhập số đầu tiên'))
def num1():
    if a < 2:
        print('không phải só nguyên tố vì nhỏ hơn 2')
    return
def num2():
    for i in range(1,a):
        i += 1
        if a%i == 0 :
            print('số này ko là số nguyên tố vì nó chia hết cho ',i)
            break
        else :
            print('số này là số nguyên tố vì ')
            break
    return
num1()
num2()