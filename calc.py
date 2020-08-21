num1 = int(input("Enter the first operand : "))
operator = input("enter the operator : ")
next_num = int(input("Enter the second operand : "))
while operator != "=":
    if operator == "+":
        result= num1+next_num          
        print("The sum of {} and {} is {}".format(num1, next_num, result))
        num1 = result       
    if operator == "*":
        result = num1*next_num
        print ("The product of {} and {} is {} ".format (num1, next_num , result))
        num1 = result 
    if operator == "-":
        result = num1 - next_num
        print("The diff of {} and {} is {}".format(num1,next_num,result))
        num1 = result      
    if operator == "/":
        result =num1 / next_num
        print ("The quo of {} and {} is {}".format(num1, next_num, result))
        num1 = result     
    operator = input("enter the operator : ")
    if operator == "=":
        break
    next_num = int(input("Enter the next operand : "))