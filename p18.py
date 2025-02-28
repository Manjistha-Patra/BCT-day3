
print("enter the number")
r=(lambda a: 1 if a==0 else a*r(a-1))(int(input()))
print("factorial",r)




# a=int(input("enter"))
# r=(lambda a: 1 if a==0 else a*r(a-1))
# b=r(a)
# print("factorial",b)

