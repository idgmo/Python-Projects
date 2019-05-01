#! python 3
# add/remove grades for multiple tests for multiple students
from statistics import mean as m

admins = {'Python':'Pass123@','user2':'Pass2'}

studentDict = {'Jeff':[78,88,93],
               'Alex':[92,76,88],
               'Sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')

    print(studentDict)



def removeStudent():
    nameToRemove = input('What student to remove?')
    if nameToRemove in studentDict:
        print('Removing student...')
        del studentDict[nameToRemove]

    print(studentDict)


def studentAVG():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,'has and average grade of', avgGrade)


def main():
    print("""
    welcome to Grade Central


    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVG()
    elif action == '4':
        exit()
    else:
        print('No valid choice was chosen, try again.')

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins [login] == passw:
        print('Welcome, ', login)
        while True:
            main()
    else:
        print('Invalid password, Self destruct activated...')
else:
    print('Invalid username, Calling FBI...')
main()