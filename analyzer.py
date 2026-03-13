#FEATURE 1 a  +
def get_text_from_input():
    user_lines= []# Empty list to store user input lines
    while True:
        raw_text = input("Enter a sentence (or 'DONE' to finish): ") # Prompt the user for input
        if raw_text.upper() == "DONE":
            break
        else:
           user_lines.append(raw_text) # this is to add the current sentence to the list of user lines
    return " ".join(user_lines) # This is to join all the lines in the list into a single string and return it
        

#FEATURE 1 b

def get_text_from_file(file_name):
    try:
        with open(file_name, 'r') as file: # Open the file in read mode
            raw_text = file.read() # Read the contents of the file
            return raw_text # Return the read text
    except FileNotFoundError:
            print (f"Error: The file was not found")
            return ""
