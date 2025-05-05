from stats import count_words
from stats import count_char

""" 
It takes a filepath as input 
and returns the contents of the file 
as a string.
"""
def get_book_text (path):
    with open(path) as f:
        text = f.read()
        return text

"""
Uses get_book_text 
with the relative path 
to your frankenstein.txt file 
to print the entire contents of the book 
to the console.
"""
def main ():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print (f"{count_words(text)} words found in the document")
    print (f"{count_char(text)}")
    

main()