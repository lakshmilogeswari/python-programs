a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(iput("enter side 3:"))
if a+b>c and a+c>b and b>+c>a:
    if a==b==c:
        print("eduilateral triangle")
    elif a==b or b==c or a==c:
        print("isosceles triangle")
    else:
        print("scalene tringle")
else:
    print("not a vaild triangle")
        
        

