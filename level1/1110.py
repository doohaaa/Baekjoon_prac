I=int(input())
n = 0
A=I//10
B=I%10
C=(A+B)%10
n=n+1
while (True) :
    A=B
    B=C
    C=(A+B)%10
    n=n+1
    if(I//10==B and I%10==C):
        print(n)
        break