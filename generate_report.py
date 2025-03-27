#!/usr/bin/env python3


  GNU nano 3.2              generate_report.py                         


# Specify the CSV file path
csv_file_path = "/home/student/data/employees.csv"  # Ensure the file $

# Call the function and store the result
employee_list = read_employees(csv_file_path)

# Print the result
print(employee_list)  # This will print the employee data

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data={}
        for department_name in set(department_list):
                department_data[department_name] = department_list.cou$
        return department_data
dictionary = process_data(employee_list)
print(dictionary)

def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k) + ':' + str(dictionary[k]) + '\$
                f.close()
write_report(dictionary, "/home/student/data/report.txt")






student@45b11b0d2bc3:~/scripts$ ./generate_report.py
[{'Full Name': 'Audrey Miller', 'Username': 'audrey', 'Department': 'Development'}, {'Full Name': 'Arden Garcia', 'Username': 'ardeng', 'Department': 'Sales'}, {'Full Name': 'Bailey Thomas', 'Username': 'baileyt', 'Department': 'Human Resources'}, {'Full Name': 'Blake Sousa', 'Username': 'sousa', 'Department': 'IT infrastructure'}, {'Full Name': 'Cameron Nguyen', 'Username': 'nguyen', 'Department': 'Marketing'}, {'Full Name': 'Charlie Grey', 'Username': 'greyc', 'Department': 'Development'}, {'Full Name': 'Chris Black', 'Username': 'chrisb', 'Department': 'User Experience Research'}, {'Full Name': 'Courtney Silva', 'Username': 'silva', 'Department': 'IT infrastructure'}, {'Full Name': 'Darcy Johnsonn', 'Username': 'darcy', 'Department': 'IT infrastructure'}, {'Full Name': 'Elliot Lamb', 'Username': 'elliotl', 'Department': 'Development'}, {'Full Name': 'Emery Halls', 'Username': 'halls', 'Department': 'Sales'}, {'Full Name': 'Flynn McMillan', 'Username': 'flynn', 'Department': 'Marketing'}, {'Full Name': 'Harley Klose', 'Username': 'harley', 'Department': 'Human Resources'}, {'Full Name': 'Jean May Coy', 'Username': 'jeanm', 'Department': 'Vendor operations'}, {'Full Name': 'Kay Stevens', 'Username': 'kstev', 'Department': 'Sales'}, {'Full Name': 'Lio Nelson', 'Username': 'lion', 'Department': 'User Experience Research'}, {'Full Name': 'Logan Tillas', 'Username': 'tillas', 'Department': 'Vendor operations'}, {'Full Name': 'Micah Lopes', 'Username': 'micah', 'Department': 'Development'}, {'Full Name': 'Sol Mansi', 'Username': 'solm', 'Department': 'IT infrastructure'}]
{'Development': 4, 'Vendor operations': 2, 'User Experience Research': 2, 'IT infrastructure': 4, 'Human Resources': 2, 'Marketing': 2, 'Sales': 3}
student@45b11b0d2bc3:~/scripts$ cd ~/data
student@45b11b0d2bc3:~/data$ ls
employees.csv  report.txt
student@45b11b0d2bc3:~/data$ cat report.txt
Development:4
Human Resources:2
IT infrastructure:4
Marketing:2
Sales:3
User Experience Research:2
Vendor operations:2
student@45b11b0d2bc3:~/data$ 