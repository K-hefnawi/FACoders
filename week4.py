def getStudentNames(class_name):
    if class_name == 'grade_one':
        for student_name in grade_one:
            print(student_name)
    elif class_name == 'grade_two':
        for student_name in grade_two:
            print(student_name)
    elif class_name == 'grade_three':
        for student_name in grade_three:
            print(student_name)
    else:
        print(class_name, 'is not a class in this school, please try using a valid class!')

def getStudentScore(class_name, student_name):
    if class_name == 'grade_one':
        if student_name in grade_one:
            results = grade_one[student_name]
            total = sum(results)
            print('Total Score:', total)
        else:
            print(student_name, 'is not a student in class grade_one!')
    elif class_name == 'grade_two':
        if student_name in grade_two:
            results = grade_two[student_name]
            total = sum(results)
            print('Total Score', total)
        else:
            print(student_name, 'is not a student in class grade_two!')

    elif class_name == 'grade_three':
        if student_name in grade_three:
            results = grade_three[student_name]
            total = sum(results)
            print(total)
        else:
            print(student_name, 'is not a student in class grade_three!')

def getStudentCount(class_name):
    if class_name == 'grade_one':
        print('Total Number of Students:', len(grade_one))
    elif class_name == 'grade_two':
        print('Total Number of Students:', len(grade_two))
    elif class_name == 'grade_three':
        print('Total Number of Students:', len(grade_three))
    else:
        print(class_name, 'is not a class in this school!')

if __name__ == '__main__':
    grade_one = {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
    grade_two = {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
    grade_three = {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

    done = False
    while not done:
        print('Choose one: students_names, student_score, students_count')
        choice = input('Choice: ').strip()
        if choice == 'students_names':
            class_name = input('Please enter class name: ').strip()
            getStudentNames(class_name)
        elif choice == 'student_score':
            class_name = input('Please enter class name: ').strip()
            student_name = input('Please enter student name: ').strip()
            getStudentScore(class_name, student_name)
        elif choice == 'students_count':
            class_name = input('Please enter class name: ').strip()
            getStudentCount(class_name)
        else:
            print("'{}' is not a valid choice!".format(choice), end = " ")

        while True:
            done_or_more = input("Choose 'done' to finish or 'more' to continue: ")
            if done_or_more == 'more':
                break
            elif done_or_more == 'done':
                done = True
                break
            else:
                print("'{}' is not a valid choice!".format(done_or_more), end = " ")
