def count_words (text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_char (text):
    count = {}
    lower = text.lower()
    for char in lower:
        if char in count:
            count[char] += 1
        else: 
            count[char] = 1
    return count
