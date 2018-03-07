import string

def puncRemove(myString):
    newString = ""
    for each in myString:
        for punc in string.punctuation:
            if punc == each:
                each = ""
        newString += each
    return newString

  
