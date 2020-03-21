# ---------------------------------------------------------- #
# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
from DataClasses import Employee

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

class DatabaseProcessor:
    '''Processes our Employee class to and from string lists that can be read and saved to files

    methods
    stringlist_to_employeelist(csvlist) -> List of Employees

    employeelist_to_listforcsv(EmpList) -> list of strings

    changelog: (When,Who,What)
        KBurdette,3.17.20,Created Class
    '''
    # TODO: Add code to process to and from a database
    @staticmethod
    def stringlist_to_employeelist(csvlist):
        '''Takes a list of strings containing employee data and converts it to employee objects

        :param csvlist:
        :return: list of employees objects
        '''
        EmpList = []
        for emp in csvlist:
            #Convert comma list of Number, First name, last name to a new employee object
            newindividual = Employee(emp[0].strip(), emp[1].strip(), emp[2].strip())
            EmpList.append(newindividual)
        return EmpList

    @staticmethod
    def employeelist_to_listforcsv(EmpList):
        '''converts employees objects to strings for text file

        :param EmpList:
        :return: list of strings containing employee data
        '''
        StrList = []
        for emp in EmpList:
            #for each Employee, use its to_string method which prints it in a row that can be easily written to text file
            StrList.append(emp.to_string())
        return StrList
