def calc():
    print("Choose one operation from the following:")
    print("1.Addition.")
    print("2.Subtraction")
    print("3.Multiplication.")
    print("4.Division.")
    print("5.Modules.")
    print("6.Square Root.")
    print("7.Exit")
    choice=int(input("Enter your choice:"))
    if choice==7:
        print("Exiting!!!!!")
        exit()
    if choice>7:
        print("invalid input!!!")
        print("Please try again!!")
        calc()
    if choice==4:
        c=int(input("Enter a number:"))
        d=int(input("Enter the second number:"))
        if d==0:
            print("Cannot be divided by 0..")
            print("Try again!!.""")
        else:
            print("The division of ",c,"by ",d,"is:",c/d)
        calc()
    if choice == 5:
        e=int(input("Enter a number:"))
        f=int(input("Enter the second number:"))
        if f==0:
            print("Cannot be divided by 0!!.")
        else:
            print("The modules of ", e, "when divided by ",f, "is:", e % f)
        calc()
    if choice==6:
        g=float(input("Enter the number:"))
        g_sqrt=g**0.5
        print("The square root of ",g," is:",g_sqrt)
        calc()
    a = int(input("Enter a number:"))
    b = int(input("Enter the second number:"))
    if choice==1:
            print("The addition of ",a,"and ",b,"is:",a+b)
            calc()
    elif choice==2:
            print("The subtraction of ",b,"from ",a,"is:",a-b)
            calc()
    elif choice==3:
            print("The multiplication of ",a,"and ",b,"is:",a*b)
            calc()
    else:
                calc()
calc()