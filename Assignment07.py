# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demos to for exception handling and pickling
# ChangeLog (Who,When,What):
# HHo,08-21-2022,created script
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "Cars.dat"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
msg_str = ""  # hold a string message
value1_str = 100  # value use in demo
value2_str = ""  # captures user input
ret_value_str = ""  # value return by processing

import pickle  # import pickle module


#  Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def divide_values(num1, num2):
        """

        :param num1: (string) numerator of division:
        :param num2: (string) denominator of division:
        :return: (string) result of division and error messages:
        """
        # try/except block
        try:
            quotient = round(float(num1) / float(num2), 2)
            msg = str(num1) + " divide by " + str(num2) + " is: " + str(quotient) + " - No Errors -- Division successful."
            return quotient, msg

        except ZeroDivisionError as e:  # handles divide by zero
            message = str(num1) + " divide by " + str(num2) + " is: Error -- Cannot divide by 0."
            return e, message

        except ValueError as e:  # handles non numeric values
            message = str(num1) + " divide by " + str(num2) + " is: Error -- Use numbers only. Cannot mix strings and numbers."
            return e, message

        except Exception as e:  # handles all other error types and provides details
            message = "Error -- Something is wrong"
            return e, message




    @staticmethod
    def read_pickle_data(file_name, data_lst):
        """

        :param file_name: (string) with name of file:
        :param data_lst: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # try/except to handle the exception of file not existing
        try:
            pickle_obj = open(file_name, "rb")
            data_lst = pickle.load(pickle_obj)
            pickle_obj.close()
            return data_lst

        except Exception as e:
            print(e, type(e), sep="\n")
            print("There was an error.  File not found. Will creating a new file.")
            pickle_obj = open(file_name, "wb")




    @staticmethod
    def add_pickle_data(make, model, year, data_lst):
        """

        :param make: (string) with name of make
        :param model: (string) with name of model
        :param year:  (string) with year
        :param data_lst: (list) to be fill with data
        :return: (lis) of dictionary rows
        """
        row = {"Make": str(make).strip(), "Model": str(model).strip(), "Year": str(year).strip()}
        data_lst.append(row)
        return data_lst



    @staticmethod
    def write_to_pickle_file(file_name, data_lst):
        """

        :param filename: (string) with name of file:
        :param data_lst: (list) you want filled with file data:
        :return: none
        """
        pickle_obj = open(file_name, "wb")
        pickle.dump(data_lst, pickle_obj)
        pickle_obj.close()
        print("Data saved (pickled) to file.")



# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_msgs(e, msg):
        """

        :param e: (string) python exception message
        :param msg: (string) custom exception message
        :return: nothing
        """
        print()  # for looks
        print(msg)
        print("Build in Python info/messages:")
        print(e, type(e), sep="\n")
        # input("\nPress Enter to continue.")
        print()  # for looks



    @staticmethod
    def print_menu():
        """
        Display a menu of choices to the user
        :return: nothing
        """
        print('''
                
                Welcome to the Exception Handling and Pickling Demo
                
                Menu of Options
                1) Exception Handling Demo
                2) Pickling Demo
                3) Exit Program        
                ''')
        print()  # Add an extra line for looks



    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice



    @staticmethod
    def print_error_demo_intro():
        """
        print intro to exception handling demo
        :return: nothing
        """
        print("\n -------- This is the Exception (Error) handling demo -------- \n")
        print("In this demo you will see how Python handles some execution errors.")
        print("A simple math operation is used to demonstrate this.\n")




    @staticmethod
    def print_pickle_demo_intro():
        """
        print intro to picking demo
        :return: nothing
        """
        print("\n -------- This is the Pickling demo -------- \n")
        print("In this demo, you will see how pickling and unpickling works.")
        print("Pickling is use to store complex data into a byte stream in binary format to a file.")
        print("Unpickling is converting the binary byte stream from the file back to its original data format.\n")



    @staticmethod
    def print_pickle_data(data_lst):
        """

        :param data_lst: (list) of rows you want to display
        :return: nothing
        """
        print("Unpickling data from the binary file.")
        print("Loading binary byte stream from the file and converting back to readable format.")
        print("Here's the un-pickled data from the file:\n")
        print("Make -- Model -- Year")
        for row in data_lst:
            print(row["Make"] + " -- " + row["Model"] + " -- " + row["Year"])



    @staticmethod
    def print_table_data(data_lst):
        """

        :param data_lst: (list) of rows you want to display
        :return: nothing
        """
        print("Here's the current and updated data in the list:\n")
        print("Make -- Model -- Year")
        for row in data_lst:
            print(row["Make"] + " -- " + row["Model"] + " -- " + row["Year"])






    @staticmethod
    def get_new_pickle_data():
        """
        Get new data from user.

        :return: (string, string, string) Make, Model and Year
        """
        make = input("Enter make of car: ")
        model = input("Enter model of car: ")
        year = input("Enter year of car: ")
        print()  # for looks

        return make, model, year



# Main Body of Script  ------------------------------------------------------ #

# Display a menu of choices to the user
while (True):
    IO.print_menu() # shows menu
    choice_str = IO.input_menu_choice()  # Get user selection

    # Process user's menu choice
    if choice_str.strip() == "1":
        IO.print_error_demo_intro()

        input("Press Enter to begin the demo.\n")
        print("Let's try dividing 100 with another value.\n")
        print("What happens if the other value is 0?\n")
        value2_str = input("Enter the number '0': ")
        ret_value_str, msg_str = Processor.divide_values(value1_str, value2_str)
        IO.print_msgs(ret_value_str, msg_str)
        input("\nPress Enter to continue.\n")

        print("What happens if the other value is non-numeric?\n")
        value2_str = input("Enter a number as a non-numeric value, i.e. 'five': ")
        ret_value_str, msg_str = Processor.divide_values(value1_str, value2_str)
        IO.print_msgs(ret_value_str, msg_str)
        input("\nPress Enter to continue.\n")

        print("What happens if the other value is a non-zero number?\n")
        value2_str = input("Enter a non-zero number: ")
        ret_value_str, msg_str = Processor.divide_values(value1_str, value2_str)
        IO.print_msgs(ret_value_str, msg_str)
        input("\nPress Enter to continue.\n")

        print("This is the end of the Exception Handling demo.")
        input("\nPress Enter to return to the main menu.\n")
        continue

    elif choice_str == "2":
        IO.print_pickle_demo_intro()

        input("Press Enter to begin demo.\n")
        print("Let's load (un-pickle) and view some pickled data from a binary file ('Cars.dat').")
        input("\nPress Enter to continue.\n")
        table_lst = Processor.read_pickle_data(file_name_str, table_lst)
        IO.print_pickle_data(table_lst)
        input("\nPress Enter to continue.\n")

        print("Let's add some new data to the list.\n")
        make, model, year = IO.get_new_pickle_data()
        table_lst = Processor.add_pickle_data(make, model, year, table_lst)
        IO.print_table_data(table_lst)
        input("\nPress Enter to continue.\n")

        print("Let's pickle the data to the file now.")
        input("\nPress Enter to continue\n")
        Processor.write_to_pickle_file(file_name_str, table_lst)
        print("Go look at 'Cars.dat' file to see the pickled data.")
        print("Looks weird, doesn't it?  It's in binary format!")
        input("\nPress Enter to continue.\n")
        print("Let's un-pickle the byte stream again to verify that the data was correctly pickled to the file.")
        input("\nPress Enter to Continue.\n")
        IO.print_pickle_data(table_lst)
        input("\nPress Enter to continue\n")

        print("This is the end of the Pickling demo.")
        input("\nPress Enter to return to the main menu\n")
        continue

    elif choice_str == "3":
        print("Exiting Program.  Goodbye!")
        break  # by exiting loop














