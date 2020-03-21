# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# KBurdette,3.17.2020,Wrote script body
# ------------------------------------------------------------------------ #
# TODO: Import Modules
import DataClasses
from IOClasses import EmployeeIO
from ProcessingClasses import FileProcessor
from ProcessingClasses import DatabaseProcessor

datafilename = "EmployeeData.txt"
EmployeeList = []

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of employee objects when script starts
EmployeeList = DatabaseProcessor.stringlist_to_employeelist(FileProcessor.read_data_from_file(datafilename))

while True:
    # Show user a menu of options
    EmployeeIO.print_menu_items()
    # Get user's menu option choice
    userpicked = EmployeeIO.input_menu_options()

    if userpicked == "1":
        # Show user current data in the list of employee objects
        EmployeeIO.print_current_list_items(EmployeeList)
    elif userpicked == "2":
        # Let user add data to the list of employee objects
        EmpObj = EmployeeIO.input_employee_data()
        EmployeeList.append(EmpObj)
    elif userpicked == "3":
        # let user save current data to file
        DidIWork = FileProcessor.save_data_to_file(datafilename,DatabaseProcessor.employeelist_to_listforcsv(EmployeeList))

        if DidIWork:
            print("Text File saved!\n")
        else:
            print("Error saving text file.\n")
    elif userpicked == "4":
        # Let user exit program
        print("Thank you for using my program!")
        break

# Main Body of Script  ---------------------------------------------------- #
