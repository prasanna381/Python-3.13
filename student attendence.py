student_id = int(input("Enter student ID: "))
student_name = input("Enter student name: ")
attendance = int(input("Enter student attendance (%): "))
subject = input("Does the student have subjects? (yes/no): ")

total_score = 0
no_subjects = 0

# Start with subject check
if subject.lower() == "no":
    print("Student has no subjects.")

elif subject.lower() == "yes":
    no_subjects = int(input("Enter number of subjects: "))

    if no_subjects == 0:
        print("No subjects entered.")
    
    elif attendance < 75:
        print("Result: Not eligible due to low attendance.")

    elif attendance >= 75:
        subject_counter = 1
        while subject_counter <= no_subjects:
            marks = int(input(f"Enter marks for subject {subject_counter}: "))
            total_score += marks
            subject_counter += 1

        print("\n--- Student Report ---")
        print(f"Student ID: {student_id}")
        print(f"Name: {student_name}")
        print(f"Attendance: {attendance}%")
        print(f"Total Score: {total_score}")
        print("Result: Eligible")

else:
    print("Invalid input for subject (please enter yes or no).")
