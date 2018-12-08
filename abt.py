n1=eval(input("Enter one number=\t"))
n2=eval(input("Enter another number=\t"))
n3=eval(input("Enter third number=\t"))

print(n1 if ((n1>n2) and (n1>n3)) else n2 if((n2>n1) and(n2>n3)) else n3 ,"big number")