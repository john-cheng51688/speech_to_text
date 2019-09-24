# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:20:12 2019

@author: john.cheng
"""
import random
from os.path import join

from pysle import isletool
from pysle import pronunciationtools

root = join(".", "files")
isleDict = isletool.LexicalTool(join(root, 'D:\Aeo_test\speech\ISLEdict.txt'))



def printOutMatches(matchStr, numSyllables=None, wordInitial='ok',
                    wordFinal='ok', spanSyllable='ok',
                    stressedSyllable='ok', multiword='ok',
                    numMatches=None, matchList=None, pos=None):

    if matchList is None:
        matchList = isleDict.search(matchStr, numSyllables, wordInitial,
                                    wordFinal, spanSyllable,
                                    stressedSyllable, multiword, pos)
    else:
        matchList = isletool.search(matchList, matchStr, numSyllables,
                                    wordInitial, wordFinal, spanSyllable,
                                    stressedSyllable, multiword, pos)
    
    if numMatches is not None and len(matchList) > numMatches:
        random.shuffle(matchList)
        
    for i, matchTuple in enumerate(matchList):
        if numMatches is not None and i > numMatches:
            break
        word, pronList = matchTuple
        pronList = ["%s(%s)" % (word, ",".join(posInfo))
                    for word, posInfo in pronList]
        print("%s: %s" % (word, ",".join(pronList)))
    print("")
    
    return matchList

# 2-syllable words with a stressed syllable containing 'dV'
# but not word initially
printOutMatches("dV", stressedSyllable="only", spanSyllable="no", wordInitial="no", numSyllables=2, numMatches=10)
print("===================================")
# 3-syllable word with an 'ld' sequence that spans a syllable boundary
printOutMatches("lBd", wordInitial="no", multiword='no', numSyllables=3, numMatches=10, pos="nn")
print("===================================")
# words ending in 'inth'
matchList = printOutMatches(u"ɪnɵ", wordFinal="only", numMatches=3)

print("===================================")
# that also start with 's'
matchList = printOutMatches("s", wordInitial="only", numMatches=3,  matchList=matchList, multiword="no")
#print(matchList)

"""
# In this first example we look up the syllabification of a word and
# get it's stress information.

searchWord = 'john'
lookupResults = isleDict.lookup(searchWord)

firstEntry = lookupResults[0][0]
firstSyllableList = firstEntry[0]
firstSyllableList = ".".join([u" ".join(syllable)
                              for syllable in firstSyllableList])
firstStressList = firstEntry[1]

print(searchWord)
print(firstSyllableList)
print(firstStressList)  # 3rd syllable carries stress
"""



"""
import speech_recognition as SR
r1 = SR.Recognizer()

with SR.AudioFile("D:/Aeo_test/speech/vox1_dev_wav_partaa/wav/id10004/6WxS8rpNjmk/00003.wav") as source:
    audio = r1.record(source)
    
print(r1.recognize_google(audio,language= "en-US"))
"""