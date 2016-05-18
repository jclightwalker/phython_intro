import urllib

def read_text():
    quotes = open (r"C:\Users\Juste Guipi\Documents\python code\text cleaner\text.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    #permet d'utiliser un site de google pour verifier s'il y a des curse word
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    #prend et affiche le teste sur le site
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!!")
    elif "false" in output:
        print("This document have no curse word!!")
    else:
        print("Can't scan the document")


    
read_text()
