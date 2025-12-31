# This is my first small project after learning basic python scripting
# The purpose of this script is to analyze a given .txt file and return key values of said file
# giving the following output: 
# 
# Total words: 128
# Unique words: 43
# Top 3:
# 1) python -> 12
# 2) world  -> 9
# 3) hello  -> 7

# Created by Fabian Harrab on Dec 31st 2025

# safely read file from path.
def read_file(path):
    try: 
        with open(path) as f:
            text = f.read()
    except FileNotFoundError:
            print(f"Error: File in location: {path} not found, check if the file is in the expected location and that it is in the .txt format.")
            return "" # ALWAYS RETURN FILETYPE SO "" for STRING
    return text

# normalize text (set lowercase and remove dots, commas, etc)
def normalize(text):
    # list of characters to check for removing
    chars = ['.', ',', '!', '?']
    # set text to lowercase
    text = text.lower()
    # check if each character from character list is present and remove
    for char in chars:
        if char in text:
            text = text.replace(char, "")
    return text

# count words
def count_words(text):
    words = {}
    text = text.split()
    for word in text:
        # add count +1 if word exist in dict
        if word in words:
            words[word] = words[word] + 1
        # create new instance in dict and set value to 1
        else:
            words[word] = 1
    return words

