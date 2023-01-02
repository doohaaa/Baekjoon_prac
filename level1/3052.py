a=1
print(a)
while True:
    a=a + a//1000 + (a%1000)//100 + ((a%1000)%100)//10 + ((a%1000)%100)%10
    if a<=10000:
        print(a)
    else : break