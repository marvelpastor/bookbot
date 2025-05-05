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
    print(get_book_text ("./books/frankenstein.txt"))
    

main()