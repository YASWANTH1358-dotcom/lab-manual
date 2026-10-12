
 
    #wite a programe to desgin a calculater
op=int(input("type :1 for addition,2 for subtraction, 3 for multiplication and 4 for division \n"));
while(op!=5):
    
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    
    if(op==1):
        print(a+b)
    elif(op==2):
        print(a-b)
    elif(op==3):
        print(a*b)
    elif(op==4):
        print(a/b)
    else:
        print("you have entered the wrong options")
    op=int(input("type :1 for addition,2 for subtraction, 3 for multiplication and 4 for division \n enter 5 to exit or enter any number to run again"))
