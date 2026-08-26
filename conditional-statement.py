marks = int(input("enter your marks: "))
if marks>=90:
    print("Grade: A")
elif marks>=70:
    print("Grade: B")
elif marks>50:
    print("Grade: C")
elif marks>=40:
     print("Grade: D")
else :
    print("fail")


    # nested if else statement

    no=  int(input("enter your number: "))
    if no>0:    
        if no%2==0:
           print("positive even number")
        else:
           print("positive odd number")
    else:
        print("number is not positive")