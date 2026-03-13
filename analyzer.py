
STOPWORDS = set([
    "the", "a", "an", "and", "is", "in", "to", "of", "it", "i", "am"
])

#Python can check if a word is in a 'set' much faster than if it were in a standard list.



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


#FEATURE 4 +
def remove_stopwords(freq_dict):    
    filtered_dict = {} # Initialize an empty dictionary to store filtered word frequencies  
    for word,count in freq_dict.items():# .items() lets us look at both the word AND its count at the same time.
        if word not in STOPWORDS:
            filtered_dict[word] = count # If the word is not a stopword, add it to the filtered dictionary with its count
    return filtered_dict


#FEATURE 5 a
# key=lambda x: x[1]: 'lambda' is a quick, nameless mini-function.
    #    'x' represents one pair, like ("apple", 5). In programming, we count starting at 0.
    #    So, x[0] is "apple", and x[1] is 5. This tells Python: "Sort these pairs by looking only at the count"
    # reverse=True: Sorts from biggest to smallest (Descending) instead of smallest to biggest.
def get_top_words(final_filter, n=10):
   
    sorted_dict = sorted(final_filter.items(), key=lambda x: x[1], reverse=True) 
    
    top_n_words = sorted_dict[:n] #slicing
    
    return top_n_words

#FEATURE 5 b
def display_report(final_filter):   
   
    total_word_count = sum(final_filter.values()) 
    
    
    unique_word_count = len(final_filter) 
    
    print(" WORD FREQUENCY REPORT ")
    print(f"Total Words: {total_word_count}")
    print(f"Unique Words: {unique_word_count}")
   
    
    # Call Top 10 function to get the data
    top_10 = get_top_words(final_filter, n=10)
    
    print("Rank | Word | Frequency")
    rank = 1
   
   # Loop through our Top 10 list and print each one out
    for word, count in top_10:
        print(f"{rank} | {word} | {count}")
        rank += 1



#FEATURE 6
def search_word(final_filter):
    word_searched = input("Enter word to be searched:")
    word_searched = word_searched.lower()
    if word_searched in final_filter:
        count = final_filter[word_searched]
        print(f"The word '{word_searched}' appeared {count} times")
    else:
        print(f"The word '{word_searched}' appeared 0 times.") 


#FEATURE 7
def export_report(raw_frequency_dict):
     # Sort all the words
     sorted_dict = sorted(raw_frequency_dict.items(), key=lambda x: x[1], reverse=True)

     with open("report.txt", "w") as file: # this opens a file and writes in it. After it gives it an alias "file"
         file.write("=== FULL WORD FREQUENCY REPORT ===\n")
         file.write("Rank | Word | Frequency\n")
         rank = 1
         for word, count in sorted_dict:
            file.write(f"{rank} | {word} | {count}\n")
            rank += 1
