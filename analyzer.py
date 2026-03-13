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



#FEATURE 2+
def clean_text(raw_text):
    cleaned_text = raw_text.lower() # Convert the text to lowercase
    punctuations = """.!()-[],{};:'","""
    for punctuation in punctuations:
        cleaned_text = cleaned_text.replace(punctuation, "") # Remove each punctuation character from the text
    cleaned_text = cleaned_text.split() # Split the cleaned text into a list of words
    return cleaned_text



#FEATURE 3 +
def count_frequences(cleaned_text):
    freq_dict = {} # Initialize an empty dictionary to store word frequencies
    for word in cleaned_text:
        if  word in freq_dict.keys(): # Check if the word is already a key in the frequency dictionary
            freq_dict[word] += 1 # If it is, increment its count by 1
        else:
            freq_dict[word] = 1 # If it is not, add it to the dictionary with a count of 1
    return freq_dict
