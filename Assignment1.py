# Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section 114
# Student Name: Brendon Antoine 
# Assignment Number: Assingment 1
# Due Date: 9/5/ 2025
# Purpose: This program creates a text based menu that allows the user to append data to an input buffer, clear the input buffer, display the contents of the input buffer, or exit the program.
# List Specific resources used to complete the assignment. I have used the VSCode auto-formatting and auto-completion tools to help me with the indentation of my code.

input_buffer = ""
user_option = ""


while user_option != '4':
    user_option = str(input("Choose an option: " \
    "\n 1. Append data to the input buffer:" \
    "\n 2. Clear the input buffer:" \
    "\n 3. Display the input buffer:" \
    "\n 4. Exit the program: "
    "\n Your choice: "))
    if user_option == '1':
        data = input("Enter data to append to the input buffer: ")
        input_buffer += data + "\n"
    elif user_option == '2':
        input_buffer = ""
        print("Input buffer cleared.")
    elif user_option == '3':
        print("Displaying input buffer contents.")
        print(input_buffer)
    elif user_option == '4':
        print("Exiting the program.")
    

