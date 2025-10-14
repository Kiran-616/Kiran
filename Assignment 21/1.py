# calculator with exception handling
def calculator():
    try:
        n1=float(input("enter first number:"))
        n2=float(input("enter second number:"))
        op=input("enter operator(+,-,*,/):")

        if op=="+":
            result=n1+n2
        elif op=="-":
            result=n1-n2
        elif op=="*":
            result=n1*n2
        elif op=="/":
            result=n1/n2
        else:
            raise ValueError("invalid operator!")
        print("result=",result)
    except ValueError as ve:
        print("error:",ve)
    except ZeroDivisionError:
        print("error:cannot divide by zero!")
    except Exception:
        print("error:invalid input!")
    
calculator()