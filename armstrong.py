n=int(input("enter the number"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("number is armstrong")
else:
    print("number is not armstrong")