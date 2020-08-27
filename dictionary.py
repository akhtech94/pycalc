vegetables = {'potato': 45,'tomato':35,'cabbage':55} 
total = 0
while True :
    vegi = input("Enter the vegetable's name or 0 to exit : ")    
    if vegi == '0':
        print("The total amount payable is {}".format(total))
        print("Thank you for using our application.")
        break
    qty = float(input("Enter the quantity : "))
    for key in vegetables.keys() :
        if vegi == key :
            total = total + vegetables[key]*qty 
            print(total)
            break