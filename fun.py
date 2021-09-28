def greater(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return("equal")
no1 = int(input("Enter no1"))
no2= int(input ("Enter no2"))
great=greater(no1,no2)
print(great)