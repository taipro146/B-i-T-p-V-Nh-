import random
a = random.randint(0,10)
b = int(input('nhập số bất kì nào : '))
print(a)
if a == b :
    print('bạn đã đoán đúng ')
else:
    print(' bạn đã đoán sai mời đoán lại ')
    for i in range(2):
        i += 1
        a1 = int(input())
        if a1 == a :
            print("bạn đã chọn đúng ")
            break
        elif i == 1:
            print('bạn đã đoán sai mời đoán lại ')
        elif i == 2:
            print('hết quyền được nhập ')

print('kết thúc chương trình ')