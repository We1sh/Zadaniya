a=int(input())
j=[]
for i in range(a):
    h=input().split()
    j.append(h)
    p=float(j[0][-1])
    q=float(j[0][-2])
    m=float(j[0][-3])
    print((p+q+m)/3)
