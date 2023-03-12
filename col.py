def colo(num):
    if num == '1':
        return "red"
    elif num == '2':
        return  "blue"
    elif num == '0':
        return "black"
    else:
        print("the Value you Enter is Worng !!!")
        num = input("Enter the number ")
        colo(num)
