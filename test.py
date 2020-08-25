vegetables = ['potato','ladiesfinger','tomato']
prices = ['20','15','12']
vegi=input("enter the vegetable name : ")
while True :  
    for index in range (3) :  
        if vegi == vegetables[index] :
            print (prices[index])
    vegi=input("enter the vegetable name : ")
    if vegi == '0':
        break
    