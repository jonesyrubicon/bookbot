path_to_file = "books/frankenstein.txt"

def main():
    
    content = readBook(path_to_file)
    wordNum = getWordLength(content)
    charHash = getCharHash(content)
    listOfHash = hashToList(charHash)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{wordNum} words found in the document")
    print()

    for dict in listOfHash:
        print(f"The {dict['char']} character was found {dict['num']} times")
        
    print("--- End report ---")


def getWordLength(txt):
    wordlist = txt.split()
    return len(wordlist)       

def readBook(path):
    with open(path) as f:
        return f.read()
    
def getCharHash(txt):
    cleanTxt = txt.replace(" ", "")
    hash = {}
    for l in cleanTxt:
        lowL = l.lower()
        if lowL in hash:
            hash[lowL] += 1
            continue
        hash[lowL] =1
    return hash

def sort_on(d):
    return d["num"]

def hashToList(hash):
    output = []
    for key in hash:
        if key.isalpha():
            output.append({"char":key,"num":hash[key]})

    output.sort(reverse=True,key=sort_on)
    
    return output



main()