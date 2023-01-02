N = int(input())
for i in range(N):
	A,B=input().split()
	A=int(A)
	B=str(B)
 
	for j in B:
		print(B[j]*A, end='')
    print()   