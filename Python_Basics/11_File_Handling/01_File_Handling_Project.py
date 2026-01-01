FILE_NAME = "students.txt"

# 1. add new students

def add_student():
     try:
          #code
          name = input("Enter student name -> ")
          email = input("Enter student email -> ")
          marks = float(input("Enter student marks -> "))
          
          with open(FILE_NAME,'a') as file:
               file.write(f"{name}, {email}, {marks}\n")
          
          print("Student record added successfully")
     except ValueError:
          print("marks must in a numeric value")    
          
     except Exception as e:
          print(e)



# 2. view Student data

def view_student():
     try:
          #code
          with open(FILE_NAME,'r') as file:
               records = file.readlines()
               
               if not records:
                    print("No student record found")
                    return
               
               print("Students record ============> ")
               
               for record in records:
                    name,email,marks = record.strip().split(',')
                    print(f"Name -> {name}, Email -> {email}, Marks -> {marks}")
     
     except FileNotFoundError:
          print("File does not exists")
     
     except Exception as e:
          print("Error -> ",e)
          


# 3. main function to execute all methods

def main():
     print("\n-- Student Management system -> ")
     print("Chose 1 to add student")
     print("Chose 2 to view all record of students")
     print("Chose 3 to Exit the program")
     
     while True:
          
          try:
               choice = int(input("Enter your choice 1 - 3 "))
               #your code
               
               if choice == 1:
                    add_student()
               elif choice == 2:
                    view_student()
               elif choice == 3:
                    print("Program exiting ")
                    break
          
          except ValueError:
               print("Enter a valid number 1 - 3")
               


main()