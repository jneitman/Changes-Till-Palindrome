#!/usr/bin/env python3

import sys

def main(argv):
    current_key = None
    current_word_list = []
    key = None
    word = None

    for line in sys.stdin:
        key, word = line.split(':', 1) #read in first line

        if current_key == key: #compiles key, tacks on incoming word
            current_word_list.append(word) #add word associated with the key 

        else:
            if current_key:
                print(current_key+ " : " + ', '.join(sorted(str(s).strip() for s in set(current_word_list)))) #print last of same key with a set of words
                current_word_list = [] #reset the list
            current_key = key #used for very fist line, and resetting to incoming new key
            current_word_list.append(word) #add new word to newly emptied list

    if current_key == key: #print out the very last line
        print(current_key + " : " + ', '.join(sorted(str(s).strip() for s in set(current_word_list))))
if __name__ == "__main__":
    main(sys.argv)
