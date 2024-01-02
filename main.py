def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    length = num_of_words(text)
    letters = num_of_letters(text)
    report(text)
    

    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

def num_of_words(text):
    return len(text.split())

def num_of_letters(text):
    text_lower = text.lower()
    split_lst = [x.lower() for x in text_lower]
    hash = {}

    for letter in split_lst:
        if letter in hash:
            hash[letter] +=1
        else:
            hash[letter] =1
    return hash

def report(text):
    text_lower = text.lower()
    split_lst = [x.lower() for x in text_lower if x.isalpha()]
    hash = {}

    for letter in split_lst:
        if letter in hash:
            hash[letter] +=1
        else:
            hash[letter] =1
            
    keys = sorted(list(dict.keys(hash)))
     
    for key in keys:
        print(f"The '{key}' character was found {hash[key]} times")

    # return  keys



main()