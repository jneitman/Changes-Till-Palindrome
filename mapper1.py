#!/usr/bin/env python3

import sys

def main(argv):

    line = sys.stdin.readline() #read in first line
    while line:
        
        def pale(start, end): #shortest distance algorithm (acts like original code, but more efficient)
            
            """ This function will find the fewest number of changes needed to make a word a palindrome.
            Resulting word will typically not be an actual word.  Has limited capability and needs additional
            companion code to account for words with special letter arrangements. 
            
            Examples:
            loop --> 1 change needed
            hello --> 2 changes needed
            
            Examples where it will fail:
            baby --> 2 changes needed where 1 change would work"""

            if start == "":
                return len(end)
            if end == "":
                return len(start)
            if start[-1] == end[-1]:
                changeCount = 0
            else:
                changeCount = 1

            res = min([pale(start[:-1], end) + 1,
                    pale(start, end[:-1]) + 1,
                    pale(start[:-1], end[:-1]) + changeCount])
            return res #end of shortest distance

        words = line.split()
        for word in words:
            word = word.lower()

            if len(word) == 1: #all words of one letter are palindromes. pale could have done this though.
                print(str(0) + ":" + word)


            elif len(word) > 1:
                
                tlist = [] #used to hold all changes for one word
                wordLen = len(word) / 2
                halfLen = (int("%d" % wordLen))
                RMcount = 0

                #working with half the word, because a palindrome is a mirror reflection of a word
                firstHalf = word[:halfLen]
                lastHalf = ''.join(list(reversed(word[-halfLen:])))
                tlist.append(pale(firstHalf,lastHalf))

                #Remove one letter then run pale to determine changes +1
                for i in range(len(word)):
                    wl = list(word)
                    del wl[i]
                    wl = ''.join(wl)
                    newLen = len(wl)/2
                    half = int("%d" % newLen)
                    FH = wl[:half]
                    LH = ''.join(list(reversed(wl[-half:])))
                    tlist.append(pale(FH,LH)+1)

                #Remove letters not in the second half of the word (removes 1 letter at a time without adding the previous removal)
                start = list(word[:int(len(word) / 2)]) #more efficient way to get half the word
                end = list(word[-int(len(word) / 2):])
                for letters in start:
                    if letters not in end:
                        RMcount += 1
                        start.remove(letters)
                        reword = start + end
                        LENGTH = int(len(reword) / 2)
                        rewordFirst = ''.join(reword[:LENGTH])
                        rewordEnd = ''.join(list(reversed(reword[-LENGTH:])))
                        tlist.append(pale(rewordFirst, rewordEnd) + RMcount)
                
                #Does the same as above, but in a different manner.
                slist = list(word)
                start = list(word[:int(len(word) / 2)])
                end = list(word[-int(len(word) / 2):])
                alist = []
                RPcount = 0
                
                for letters in start:
                    if letters not in end:
                        alist.append(letters)

                for i in alist:
                    if i in slist:
                        RPcount += 1
                        slist.remove(i)
                        t = slist
                        first = ''.join(list(t[:int(len(t) / 2)]))
                        last = ''.join(list(reversed(t[-int(len(t) / 2):])))
                        tlist.append(pale(first,last) + RPcount)


                #Obtain the smallest number of changes
                print(str(min(e for e in tlist)) + ":" + word)
        line = sys.stdin.readline()
if __name__ == "__main__":
    main(sys.argv)