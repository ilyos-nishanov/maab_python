#
while True:
  command = input("MENU:\n\t1. Student List\n\t2. Subjects list\n\t3. Grades by ID\n\t4. Exit\n")
  if command == '4':
    break
  
  # list the students and register new entries
  elif command == "1":
    print(f"StudentID Name\n")
    for id, value in students.items():
      print(f"{id} {value['name']}")
    print("\n")
    
    #new entry
    command = input("1. Add Student\n2. Back to menu")
    if command == "1":
      name = input("Student name: ")
      students[max(list(students.keys()))+1] = {"name": name, "subjects": subjects}
    else:
        command = input("MENU:\n\t1. Student List\n\t2. Subjects list\n\t3. Grades by ID\n\t4. Exit\n")
        if command == '4':
            break
          
  # list subjects and register new entries
  elif command == "2":
    print(f"SubjectID Name\n")
    for id, value in subjects.items():
      print(f"{id} {value}")
    print("\n")
    
    #new entry
    command = input("1. Add Subject\n2. Back to menu")
    if command == "1":
      name = input("Subject name: ")
      subjects[max(list(subjects.keys()))+1] = name
    else:
        command = input("MENU:\n\t1. Student List\n\t2. Subjects list\n\t3. Grades by ID\n\t4. Exit\n")
        if command == '4':
            break
          
  #list grades and register new entries
  elif command == "3":
    for student_id, subject_grades in grades.items():
      student_name = students[student_id]["name"]
      print(f"Student: {student_name}")
      for subject_id, grade in subject_grades.items():
        subject_name = subjects[subject_id]
        print(f"  Subject: {subject_name}, Grade: {grade}")
    command = input("1. Add grade\n2. Back to menu")
    
    #new entry
    if command == "1":
      st_id = int(input("Student id: "))
      subject_id = int(input("Subject id: "))
      grade = int(input("grade: "))
      if st_id in grades:
        grades[st_id][subject_id] = grade
      else:
        grades[st_id] = {subject_id: grade}
    else:
        command = input("MENU:\n\t1. Student List\n\t2. Subjects list\n\t3. Grades by ID\n\t4. Exit\n")
        if command == '4':
            break