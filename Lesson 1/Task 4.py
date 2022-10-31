a = int(input("Input a:"))
b = int(input("Input b:"))
c = int(input("Input c:"))
D = b**2-(4*a*c)
if D>0:
    x1 = (-b + (D**(1/2)))/(2*a)
    x2 = (-b - (D**(1/2)))/(2*a)
    print("x1=",x1,'\n' "x2=",x2)
elif D == 0:
    x1 = (-b)/(2*a)
    print("x= ",x1)
else:
    print("No Radical")