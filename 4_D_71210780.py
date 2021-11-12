#S11 dari deret 1, 3, 9, 27,....

#input
u1= 1
u2= 3
u3= 9
n= 11

#proses
a= u1
r= u2/u1
x= (a*(r**n-1))/(r-1)

#output
print("Jumlah suku ke", n, "adalah", x)
