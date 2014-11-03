def loadWords2():
    try:
        inFile = open('sd', 'r', 0)
    except IOError:
    #except: except IOError: except ValueError as e: except FileNotFound: except IOError as e: 
    #line of code to be added here#
        print "The wordlist doesn't exist; using some fruits for now"
        return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist
    
loadWords2()