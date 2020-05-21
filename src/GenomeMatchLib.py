import collections
import operator


# patternCount
# Paramenters:  content - this is the string representing

def patternCount(content, pattern):
    count = 0
    contentLength = len(content)
    patternLength = len(pattern)
    scanLength = contentLength - patternLength
    scanPointer = 0
    while scanPointer < scanLength:
        text = content[scanPointer:(scanPointer+patternLength)]
        if (text == pattern):
            count += 1
        scanPointer += 1
    return count



def frequentWords(text, k):
    freqDict = {}
    scanPointer = 0
    scanLength = len(text) - k
    while scanPointer < scanLength:
        pattern = text[scanPointer:(scanPointer+k)]
        if not(pattern in freqDict):
            count = patternCount(text, pattern)
            freqDict[pattern] = count
        scanPointer += 1
    sortedDict = collections.OrderedDict(sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True))
    maxValue = 0
    maxPattern = ''
    for kmer in sortedDict:
        if (sortedDict[kmer] >= maxValue):
            maxValue = sortedDict[kmer]
            if (maxPattern == ''):
                maxPattern = kmer
            else:
               maxPattern = maxPattern + ' ' + kmer
        elif (sortedDict[kmer] < maxValue):
            break
    return maxPattern

def patternIndex(pattern, genome):
    genIndex = ''
    scanLength = len(genome) - len(pattern)
    genScanner = 0
    segment = ''
    while (genScanner <= scanLength):
        segment = genome[genScanner:genScanner+len(pattern)]
        if (segment == pattern):
            if (genIndex == ''):
              genIndex += str(genScanner)
            else:
               genIndex += ' ' + str(genScanner)
        genScanner += 1
    return genIndex


def reverseComplement(sequence):
    posCounter = 0
    complement = ''
    while (posCounter < len(sequence)):
        if(sequence[posCounter] == 'A'):
            complement += 'T'
        elif (sequence[posCounter] == 'T'):
            complement += 'A'
        elif (sequence[posCounter] == 'G'):
            complement += 'C'
        elif (sequence[posCounter] == 'C'):
            complement += 'G'
        posCounter += 1
    return (''.join(reversed(complement)))




