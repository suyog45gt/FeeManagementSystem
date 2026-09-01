# School Fee Management System
import json
fee=[]
class_fee = {
    "Nursery": 1800,
    "LKG": 1900,
    "UKG": 2000,
    "Class 1": 2100,
    "Class 2": 2200,
    "Class 3": 2300,
    "Class 4": 2400,
    "Class 5": 2500,
    "Class 6": 2600,
    "Class 7": 2700,
    "Class 8": 2800,
    "Class 9": 2900,
    "Class 10": 3000,
    "Class 11": 3100,
    "Class 12": 3200
}
transport_fee = 500
hostel_fee = 10000
def student_info():

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    class_name = input("Enter class (Nursery, LKG, UKG, Class 1-12): ")
    contact_info = input("Enter contact information: ")
    
    student_record = {
        "name": name,
        "roll_no": roll_no,
        "class": class_name,
        "contact_info": contact_info,
    }
    
    fee.append(student_record)
    with open("students_data.json", "w") as f:
        json.dump(fee, f, indent=4)
    print("Student information saved successfully.")
    return student_record

def total_fee(student_record):
    class_name = student_record.get("class")
    transport = input("Does the student require transport? (yes/no): ").lower()
    hostel = input("Does the student require hostel? (yes/no): ").lower()
    
    base_fee = class_fee.get(class_name, 0)
    total = base_fee
    
    if transport == "yes":
        total += transport_fee
    if hostel == "yes":
        total += hostel_fee

    with open("student.txt", "w") as f:
        f.write("---------- FEE DETAILS ----------\n")
        f.write("---------------------------------\n")
        f.write(f"Student Name: {student_record['name']}\n")
        f.write(f"Roll Number: {student_record['roll_no']}\n")
        f.write(f"Class: {class_name}\n")
        f.write(f"Contact: {student_record['contact_info']}\n")
        f.write(f"Base Fee: Rs. {base_fee}\n")
        f.write(f"Transport Fee: Rs. {transport_fee if transport == 'yes' else 0}\n")
        f.write(f"Hostel Fee: Rs. {hostel_fee if hostel == 'yes' else 0}\n")
        f.write(f"Total Fee: Rs. {total}\n")
        f.write("---------------------------------\n")
    with open("student.txt", "r") as f:
        print(f.read())
student=student_info()
total_fee(student)


