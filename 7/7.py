a = int(input('nhập số a'))
c = list(range(1,a+1))
def songuyento(n):
    if (n<2):
        return False
    i = 2;
    while i <= n / 2:
        if (n % i == 0):
            return False
        i += 1
    return True
for i in c:
    if songuyento(i):
        print(i ,end = ' ')