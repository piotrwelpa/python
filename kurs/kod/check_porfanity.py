import urllib

def read_text():
    quotes = open("/home/pwelpa/Desktop/python/kurs/pliki/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse word!")
    else:
        print("Could not scan the document properly")
                
read_text()
