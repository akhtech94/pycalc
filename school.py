students = {
    '1':{'name': 'Sreeshma', 'marks': '95', 'phonen0': '9656795252', 'email': 'sreeshma739@gmail.com'},
    '2':{'name':'Akhil','marks':'90','phoneNO':'7403505273','Email':'akhilkannan1994@gmail.com'}}

Action = input('Enter d to display one or m to Modify or da to Display all:')
if Action == 'd':
    RollNo = input('Enter the RollNo of  Student : ')
    for val in students[RollNo] :
        print("{} : {}".format(val, students[RollNo][val]))
if Action == 'm' :
    RollNo = input('Enter the RollNo of  Student : ')
    for val in students[RollNo] :
        print("{} : {}".format(val, students[RollNo][val]))
    NewVar = input('Enter The New Mark : ')
    students[RollNo]['marks'] = NewVar
    print('The Updated Details are : ')
    for val in students[RollNo] :
        print("{} : {}".format(val, students[RollNo][val]))
if Action == 'da' :
    for RollNO in students:
        for val in students[RollNO]:
            print("{} : {}".format(val, students[RollNO][val]))
