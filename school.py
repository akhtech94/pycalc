from data import students

found = False

print('Press D for Display One student details ')
print('Press M for Modify')
print('Press DA for Display all Details')
action = input()
action = action.capitalize()

if action == 'D':
    user_rollno = int(input('Enter the RollNo : '))
    for dict in students:
        if dict['rollno'] == user_rollno:
            found = True
            for key, val in dict.items():
                print("{} : {}".format(key, val))
    if found == False:
        print("Sorry, we could not find any record with the roll number you specified.")
