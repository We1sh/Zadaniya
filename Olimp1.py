a=int(input())
j=[]
for i in range(a):
    h=input().split()
    j.append(h)
    g=str(j)[1:-1]
    print((float(g[-4:-2])+float(g[-10:-8])+float(g[-16:-14]))/3)
